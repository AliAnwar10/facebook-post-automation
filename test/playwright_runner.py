import asyncio
from playwright.async_api import async_playwright
from db_Insert import get_credentials, get_selected_posts

async def run_automation(credential_id):
    async with async_playwright() as playwright:
        # Get credentials
        credentials = get_credentials()
        if not credentials:
            print("No credentials found.")
            return
        _, email, password = credentials[credential_id-1] 

        # Persistent session
        
        context = await playwright.chromium.launch_persistent_context(
            user_data_dir="user_data",
            headless=False,
        )
        page = context.pages[0] if context.pages else await context.new_page()

        logged_in = False
        try:
            await page.goto("https://www.facebook.com/", timeout=60000)
            await page.wait_for_selector("input[name='email']", timeout=5000)

            print("Logging in...")
            await page.fill("input[name='email']", email)
            await page.fill("input[name='pass']", password)
            await page.click("button[name='login']")

            print("Waiting for login to complete (and 2FA if needed)...")
            await page.wait_for_url("https://www.facebook.com/", timeout=180000)
            await asyncio.sleep(5)
            logged_in = True
            print("Login successful. Session saved.")
        except:
            print("Already logged in (session loaded).")
            await page.screenshot(path="screenshot.png")

            await asyncio.sleep(2)

        # Get selected group-post pairs
        selections = get_selected_posts(credential_id)
        for index, (group_name, group_url, title, description, hashtags, image_path) in enumerate(selections):
            group_page = await context.new_page()
            await group_page.goto(group_url, timeout=120000)
            await group_page.wait_for_load_state('networkidle')
            print(f"\nOpened group {index + 1}: {group_name} ({group_url})")

            write_xpath = "//div[@role='button']//span[contains(text(), 'Write something')]"
            post_xpath = "//div[@role='textbox' and @contenteditable='true' and contains(@aria-placeholder, 'Create a public post')]"

            await group_page.wait_for_selector(f"xpath={write_xpath}", timeout=150000)
            await group_page.click(f"xpath={write_xpath}")
            print("Clicked 'Write something...'")

            await group_page.wait_for_selector(f"xpath={post_xpath}", timeout=100000)
            post_input = await group_page.query_selector(f"xpath={post_xpath}")
            await post_input.click()
            post_content = f"{title}\n\n{description}\n\n{hashtags}"
            await post_input.fill(post_content)
            print("Post content filled.")

            # image
            if image_path:
                try:
                    await group_page.set_input_files("input[type='file']", image_path)
                    print(f"Uploaded image: {image_path}")
                    await asyncio.sleep(5) 
                except:
                    print(f"Failed to upload image: {image_path}")

            post_button_xpath = "//div[@role='button' and @aria-label='Post']"
            await group_page.wait_for_selector(f"xpath={post_button_xpath}", timeout=10000)
            await group_page.click(f"xpath={post_button_xpath}")
            print(f"Post {index + 1} submitted!")
            await page.screenshot(path="screenshot1.png")

            if index != len(selections) - 1:
                print("Waiting 30 seconds before next post...")
                await asyncio.sleep(30)

        await context.close()
        print("All done completed.")