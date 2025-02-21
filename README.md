# # Secure Open Source Training Repository

## Repository Overview
This repository is designed for hands-on exercises to learn how to secure open-source projects. It contains:

- **Hardcoded secrets** for testing GitHub Secret Scanning
- **Outdated dependencies** flagged by Dependabot
- **Code vulnerabilities** detected by CodeQL
- **No branch protection rules** (so learners can enable them manually)

---

## Hands-on Exercises

### 1. Detecting and Rotating Secrets (Secret Scanning)
#### Steps:
1. **Fork this repository** to your GitHub account.
2. Go to `config.py` and observe the hardcoded API key.
3. Enable **Secret Scanning** in your repository settings (`Settings > Security > Secret Scanning`).
4. GitHub should flag the hardcoded secret. Once detected, **rotate and remove** the secret:
   - Delete the secret from `config.py`
   - Use `git rebase -i` or `BFG Repo-Cleaner` to remove it from history.
   - Commit and push the cleaned code.

---

### 2. Updating Dependencies (Dependabot)
#### Steps:
1. Enable **Dependabot alerts and security updates** (`Settings > Security > Dependabot`).
2. Open `requirements.txt` (Python) and notice the outdated dependencies.
3. Run:
   ```bash
   pip install --upgrade -r requirements.txt  # Python
   npm update  # JavaScript
   ```
4. Create a **pull request (PR)** with updated dependencies and merge it.

---

### 3. Running Code Scanning (CodeQL)
#### Steps:
1. Enable **Code Scanning** in your repository (`Settings > Security > Code Scanning`).
2. Set up a **GitHub Actions workflow** using the `.github/workflows/codeql-analysis.yml` file.
3. Review the vulnerabilities flagged by **CodeQL**.
4. Fix any **SQL injection** or **unsafe deserialization** issues in `vulnerable.py`.

---

### 4. Configuring Branch Protection
#### Steps:
1. Go to `Settings > Branches` in your repository.
2. Click **"Add Rule"** and apply the following:
   - Require pull requests before merging.
   - Require at least **one review** before merging.
   - Require **status checks to pass** before merging.
3. Save changes and test by attempting a direct push to `main` (it should be blocked!).

---

### 5. Handling a Security Report (Coordinated Vulnerability Disclosure)
#### Steps:
1. Navigate to `SECURITY.md` and review how to report security issues.
2. Create an issue following **responsible disclosure guidelines**.
3. Simulate a security fix by applying a patch and closing the issue.

---
## Repository Structure
```
/
├── config.py  # Contains a hardcoded API key for Secret Scanning detection
├── vulnerable.py  # Code with SQL injection & unsafe deserialization for CodeQL scanning
├── requirements.txt  # Outdated dependencies for Dependabot alerts
├── SECURITY.md  # Instructions for vulnerability disclosure
├── .github/
│   ├── workflows/
│   │   ├── codeql-analysis.yml  # GitHub Actions for CodeQL scanning
```
## Next Steps
1. **Follow each exercise** step by step.
2. **Fix issues** flagged by GitHub security tools.

Happy Securing! 🔒

---
