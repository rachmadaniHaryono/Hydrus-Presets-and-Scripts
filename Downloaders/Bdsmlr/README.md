[See the help files for how to add downloaders to Hydrus](https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html)

## What is this
A guide to help you get successfully setup with the bdsmlr downloader components.

## IMPORTANT NOTE
_**The bdsmlr downloader requires adding authenticated cookies from a bdsmlr account with specific settings into the Hydrus client - it does not work at all without them!**_ (see below)

## How to get this working
### Prequisites
**you will need all of these things for these parsers to work**
- Be on Hydrus v435 or later
- In the Hydrus client, under 'options'->'connections', make sure the checkbox for 'BUGFIX: verify regular https traffic' is to be **unchecked**.
- Have a working bdsmlr.com login (ideally not your main one)
- Know how to add session cookies to your Hydrus client
  - I recommend using the [Hydrus Companion](https://gitgud.io/prkc/hydrus-companion) browser extension for this. Once you've got it installed and connected to your Hydrus client, look in the extension for it's help pages and search for cookies to find instructions on how to send them to Hydrus.

### Setup
The big trick to getting this downloader working is to choose the right settings on your bdsmlr account and then send those cookies over to the Hydrus client. **_Without the account settings being set the right way, and without Hydrus having those cookies, the downloader will not work_**. 

Once you're logged into bdsmlr.com, go to the settings for your account, and make sure the following options (highlighted in red) are **enabled** (aka, check the checkboxes) for your account:
<img width="856" alt="bdsmlr_account_settings" src="https://user-images.githubusercontent.com/65079055/115484486-e637c580-a220-11eb-8e4a-f065daaf553c.png">

After you've saved your settings, go to your favorite blog and scroll to the bottom. You should see "previous" and "next" buttons instead of having more posts auto-load - if you see them, good, that's what you want. Send those bdsmlr cookies from your browser over to Hydrus (via HydrusCompanion or some other way), and things should be working. We're not sure how long bdsmlr session cookies last, though, so send over new ones if things stop working.

### Troubleshooting
Here's at least a couple things to try if the downloader isn't working properly:
 - Clear your Hydrus session cookies and run through the setup again, making sure you've got everything set properly
 - Delete all of the downloader network components from your Hydrus client and re-import the downloader image
   - See the list below. You can find the downloader components in various windows found in the 'network->downloader components' menu in the Hydrus client.

### Components description (aka extra stuff if you wanna try iterating or just understanding it)
This downloader provides the following:
- A simple GUG for crawling a bdsmlr blog (requires all the below items)
- Blog page **parser**: parses a single blog page (with a `?page=1` query param) for individual post permanlinks
- Post page **parser**: parses a single post permalink for images and videos, and sometimes tags (see section about tags below)
- Blog page **URL class**: takes a standard blog URL and ensures it has a `?page={NUMBER}` query param. Defaults to if there's no number already. Tells the GUG that the next "gallery" page can be found by incrementing the NUMBER.
- Post page **URL class**: just a URL class for a blog post permalink page. Doesn't do anything fancy, but it means you can pass a url for specific posts into the Hydrus' URL downloader.
- File **URL class**: similar to the above, means you can pass a direct bdsmlr file link into Hydrus' URL downloader.

### Disclaimer
bdmslr is, from a technical and parsing standpoint, a giant mess that changes often so this downloader is not guaranteed to work. Having some experience with parsing and downloaders for other sites is recommended before trying this one. If you find it's not working for you, try messing around with the components to see if you can find what's going wrong and fix it. If you can fix it, feel free to let us know or submit a pull request to update the stuff on this repo.

Also, this downloader does not include bandwidth rules, but I've found that bdsmlr has a tendency to throttle pretty quick and/or just be pretty slow in general, just as a heads up. If you can somehow get regular download speeds that are over 1MB/s, let us know how.
