# Setup guide for new editors

This guide takes you from a fresh computer to making your first published
edit to the live site. No prior programming experience needed. Allow
about 30 minutes.

When you're done your VSCode window will look like this:

```
+----------+--------------------------------+-----------------+
|          |                                |                 |
|  Files   |  Simple Browser                |  Claude Code    |
|  (left)  |  http://127.0.0.1:8000         |  (right)        |
|          |                                |                 |
|  docs/   |  +--------------------------+  |  > Add a        |
|   ...    |  |   AESPD Deliverables    |  |    sentence...  |
|          |  |   [the live preview]    |  |                 |
|          |  +--------------------------+  |  Claude writes  |
|          |                                |  the change.    |
|          +--------------------------------+                 |
|          |  Terminal                      |                 |
|          |  $ mkdocs serve                |                 |
|          |  Serving on 127.0.0.1:8000     |                 |
+----------+--------------------------------+-----------------+
```

You edit by talking to Claude on the right; the live preview in the
center updates within a second; the terminal at the bottom is where you
run a couple of commands when you're ready to publish.

---

## What you'll need

- A computer running macOS, Windows 10/11, or Linux
- An email address
- About 1.5 GB of free disk space
- Network access

---

## Part 1 — Create accounts (one-time)

### 1.1 GitHub account
1. Go to <https://github.com> and click **Sign up**.
2. Use your real name on the profile — your commits will be attributed
   to it.
3. Verify your email.
4. Send your GitHub username to the project owner so they can add you
   as a collaborator on
   <https://github.com/Takhleeq-ASEPD/AdvancedSystemsEngineering-ProposalDevelopment>.
5. When the invitation arrives in your email, click **Accept**.

### 1.2 Anthropic / Claude account
1. Go to <https://claude.ai> and sign up (or sign in if you already have
   one).
2. If you don't already have access to Claude Code, the project owner
   will tell you which plan or API key to use. Don't pay for anything
   on your own without checking.

---

## Part 2 — Install software (one-time)

Pick your operating system below and follow that section only.

### macOS

1. Install **Homebrew** (the package manager). Open **Terminal**
   (search Spotlight for "Terminal") and paste:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   Follow the prompts. It may ask for your Mac password.
2. Install everything else:
   ```bash
   brew install git python@3.12 gh
   brew install --cask visual-studio-code
   ```

### Windows 10/11

1. Open **PowerShell as Administrator** (right-click Start → "Terminal
   (Admin)" or "Windows PowerShell (Admin)").
2. Install everything:
   ```powershell
   winget install --id Git.Git
   winget install --id Python.Python.3.12
   winget install --id Microsoft.VisualStudioCode
   winget install --id GitHub.cli
   ```
3. Close and reopen PowerShell so the new commands are recognised.

### Linux (Ubuntu / Debian)

In a terminal:
```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
# VSCode:
sudo snap install --classic code
# GitHub CLI (gh):
sudo apt install -y gh
```

If `apt install gh` fails (older Ubuntu), follow
<https://github.com/cli/cli/blob/trunk/docs/install_linux.md>.

---

## Part 3 — Verify the installs

Open a fresh terminal (close any old ones first) and run these one at a
time:

```bash
git --version
python --version
code --version
gh --version
```

Each should print a version number (e.g. `git version 2.43.0`). If any
says "command not found":
- macOS / Linux: close and reopen the terminal.
- Windows: close and reopen PowerShell. If still failing, run the
  matching `winget install` command again and pay attention to any
  warnings.

On Windows, `python` may show as `python3` or open the Microsoft Store.
If that happens, run:
```powershell
py --version
```
and use `py` instead of `python` everywhere below.

---

## Part 4 — Connect Git to GitHub (one-time)

In your terminal:
```bash
gh auth login
```

You'll see a series of prompts. Answer them in order:

| Prompt | Answer |
|---|---|
| Where do you use GitHub? | **GitHub.com** |
| What is your preferred protocol for Git? | **HTTPS** |
| Authenticate Git with your GitHub credentials? | **Yes** |
| How would you like to authenticate? | **Login with a web browser** |

A short code (e.g. `XXXX-XXXX`) appears. Press **Enter** — a browser
window opens. Paste the code, click **Authorize**, close the browser
tab. Back in the terminal you should see `✓ Authentication complete`.

Verify:
```bash
gh auth status
```
Should print `✓ Logged in to github.com account YOUR-USERNAME`.

Set your name and email for commits (so your work is attributed to you):
```bash
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"
```
Use the same email as your GitHub account.

---

## Part 5 — Get the project

Pick a folder where you keep code (anything you like, e.g.
`~/projects` on Mac/Linux or `Documents\Code` on Windows). In the
terminal:

```bash
cd ~/projects                    # or wherever you chose
gh repo clone Takhleeq-ASEPD/AdvancedSystemsEngineering-ProposalDevelopment
cd AdvancedSystemsEngineering-ProposalDevelopment
```

You're now inside the project folder.

---

## Part 6 — Install project dependencies

Still in the project folder:

```bash
python -m venv .venv
```

This creates a private folder of Python tools for this project only.
Now activate it:

- **macOS / Linux**:
  ```bash
  source .venv/bin/activate
  ```
- **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
  If PowerShell complains about "scripts are disabled", run this once
  and try again:
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```

After activation your prompt should start with `(.venv)`. Now install
the project's tools:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Verify:
```bash
mkdocs --version
```
Should print `mkdocs, version 1.6.x ...`.

---

## Part 7 — Set up VSCode

### 7.1 Open the project
1. Start **Visual Studio Code**.
2. **File → Open Folder…** → select the
   `AdvancedSystemsEngineering-ProposalDevelopment` folder you just
   cloned.
3. If VSCode asks "Do you trust the authors of the files?" → **Yes**.

### 7.2 Install the Claude Code extension
1. Click the **Extensions** icon in the activity bar on the left (four
   squares) — or press **Ctrl+Shift+X** (**Cmd+Shift+X** on Mac).
2. Search for **Claude Code**.
3. Click **Install** on the extension published by **Anthropic**.
4. After install, click the Claude Code icon that appears in the left
   activity bar and follow the sign-in prompt.

### 7.3 Move Claude Code to the right side
By default Claude Code opens on the left. To move it:
1. Right-click the **Claude Code** icon in the left activity bar.
2. Choose **Move to Secondary Side Bar**.

It now lives on the right side of the window. You can drag the border
between the right panel and the editor to make it wider/narrower.

### 7.4 Start the local site
1. **View → Terminal** (or press **Ctrl+`** — the backtick, top-left
   of your keyboard).
2. Make sure the prompt starts with `(.venv)`. If not, run the
   activate command from Part 6 again.
3. In the terminal, run:
   ```bash
   mkdocs serve
   ```
4. Wait until you see:
   ```
   INFO    -  Serving on http://127.0.0.1:8000/
   ```
5. **Leave this terminal running.** It's the live-preview server. If
   you close it, the preview stops working.

### 7.5 Open the live preview in the center
1. Press **Ctrl+Shift+P** (**Cmd+Shift+P** on Mac) to open the Command
   Palette.
2. Type **Simple Browser: Show** and press **Enter**.
3. When prompted for a URL, type `http://127.0.0.1:8000` and press
   **Enter**.
4. The site appears as a tab in the centre editor area.

### 7.6 Open a second terminal (optional but useful)
The terminal running `mkdocs serve` is busy — you can't type commands
into it. To run git commands without stopping the preview, open a
second terminal:
1. In the bottom terminal panel, click the **+** icon (top right of
   the panel).
2. A new terminal opens beside the first. Use this one for git
   commands.

You now have the target layout: files on the left, live preview in the
centre, Claude Code on the right, terminal at the bottom.

---

## Part 8 — Your first edit

1. In the file tree on the left, expand `docs/` →
   `stages/` → `1-requirements/`.
2. Click `d1-list-of-stakeholders.md` to open it in the editor.
3. In the Claude Code panel on the right, type something like:
   > Add a sentence at the very end of this file saying "Last edited
   > by Your Name on today's date" and update the `last_reviewed` date
   > in the front matter.
4. Press Enter. Claude reads the file, makes the edit, and tells you
   what it changed.
5. Look at the Simple Browser tab in the center — the change should
   appear within a second. If not, click the refresh button on the
   Simple Browser tab.

That's the loop. Edits are local-only at this point; the public site is
unchanged.

---

## Part 9 — Publishing your edit

When you're happy with the change, open the **second terminal** (the
one not running `mkdocs serve`) and run these commands one at a time:

```bash
# Create a branch to hold your edits (acts as a save point):
git checkout -b edit/my-first-edit

# Stage and commit your changes:
git add docs/stages/1-requirements/d1-list-of-stakeholders.md
git commit -m "Add my name to stakeholders deliverable"

# Switch back to the main branch and merge:
git checkout main
git pull                       # in case someone else published in the meantime
git merge edit/my-first-edit

# Publish:
git push
```

The `git push` is the publish step. The GitHub Action takes about a
minute to rebuild and deploy.

### Watch the deploy
```bash
gh run watch
```
This streams the deploy progress. When it finishes, refresh the live
site:
<https://takhleeq-asepd.github.io/AdvancedSystemsEngineering-ProposalDevelopment/>

Your edit should be visible. Done.

(If you'd rather just watch in a browser, the status page is
<https://github.com/Takhleeq-ASEPD/AdvancedSystemsEngineering-ProposalDevelopment/actions/workflows/deploy.yml>.)

---

## Daily routine (after first-time setup)

Every editing session:

1. Open VSCode → the project folder.
2. Activate the venv in your terminal (see Part 6) — only needed once
   per terminal.
3. Pull the latest:
   ```bash
   git checkout main
   git pull
   ```
4. Start a new branch for this session:
   ```bash
   git checkout -b edit/<short-description>
   ```
5. Start the preview server and open the browser tab (Parts 7.4 and
   7.5). If they're still running from earlier, skip.
6. Edit via Claude in the right panel.
7. When done:
   ```bash
   git add <files-you-changed>
   git commit -m "What you changed"
   git checkout main
   git pull
   git merge edit/<short-description>
   git push
   ```

---

## Troubleshooting

**"command not found" after installing**
Close and reopen the terminal. On Windows, close and reopen PowerShell
(and possibly VSCode too).

**`mkdocs serve` says "Address already in use"**
Another preview is already running. Find the terminal where it's
running and press **Ctrl+C**. If you can't find it:
- macOS / Linux: `pkill -f "mkdocs serve"`
- Windows: close all VSCode windows and reopen.

**Git asks for a password**
You skipped `gh auth login`. Go back to Part 4. If you've done that and
it still asks, run `gh auth status` to confirm — if it says "not
logged in", redo Part 4.

**Claude Code says "Not authenticated"**
Click the Claude icon and follow the sign-in prompt. If sign-in fails,
ask the project owner about your access.

**My change isn't on the live site after pushing**
1. Open
   <https://github.com/Takhleeq-ASEPD/AdvancedSystemsEngineering-ProposalDevelopment/actions/workflows/deploy.yml>
2. Green check next to your push = it worked; clear browser cache and
   try again (Ctrl+F5 / Cmd+Shift+R).
3. Red X = deploy failed; click into the run and copy the error
   message to send to the project owner.

**My terminal doesn't show `(.venv)`**
You need to activate the virtual environment again. Run the activate
command from Part 6 in this terminal.

**`git push` says "rejected"**
Someone else pushed while you were editing. Run:
```bash
git pull --rebase
git push
```
If git complains about conflicts, ask for help — don't try to resolve
manually until you've done this once with someone watching.

---

## Where to go next

- **What lives where in the repo**: see `README.md`
- **Editing conventions** (file names, comment format, table rules,
  diagrams, images): see `CLAUDE.md` — both you and Claude follow it
- **What's in the deliverables**: read the live site itself,
  <https://takhleeq-asepd.github.io/AdvancedSystemsEngineering-ProposalDevelopment/>
