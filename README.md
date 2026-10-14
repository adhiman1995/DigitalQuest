# DigitalQuest (ESE ECE Tracker)

Syllabus coverage tracker, a typeset previous-year question library, and a timed exam mode.
React (Vite) frontend, Node/Express backend, Google sign-in, progress saved per account in Postgres.

## Run locally
```bash
npm install && npm run build
cp .env.example .env        # optional; without GOOGLE_CLIENT_ID you get a "Dev sign-in" box
npm run dev:server          # http://localhost:3001
```
For hot reload run `npm run dev:client` too and open http://localhost:5173.
Tests: `npm test`.

## Deploy to Render
1. Push this folder to a GitHub/GitLab repo (the repo root should be this `ese-tracker` folder).
2. **Google Cloud Console** → APIs & Services → Credentials → *Create credentials* → **OAuth client ID** → *Web application*.
   - *Authorized JavaScript origins*: `https://<your-service>.onrender.com` (and `http://localhost:3001` for local testing).
   - No redirect URI is needed (the Google button uses a popup + ID token).
   - If asked, configure the OAuth consent screen first (External, add your email as a test user while in *Testing*).
3. **Render** → New → **Blueprint** → select the repo. It creates the web service and the `ese-db` Postgres database
   and wires `DATABASE_URL` and a generated `SESSION_SECRET` automatically.
4. In the web service's *Environment* tab set `GOOGLE_CLIENT_ID` to the client ID from step 2, then redeploy.
5. Open the service URL, click **Sign in with Google**.

Notes
- Render's free web service sleeps when idle (first request is slow). Free Postgres is time-limited; upgrade the database plan to keep accounts and progress permanently.
- Progress works without signing in (stored in the browser). Signing in saves it to your account and syncs across devices.

## Adding questions
Drop images into `../question-bank/<paper>/<subject>/<chapter>/`, then follow `scripts/authoring/README.md`.
`node scripts/scan.js` shows what has been processed. Commit the changed `server/data/*.json` and redeploy.
