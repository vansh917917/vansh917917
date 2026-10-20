![header](https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:2c5364,100:6a11cb&height=240&section=header&text=Vansh%20Gupta&fontSize=55&fontAlign=50&fontAlignY=35&fontColor=EAEAEA&desc=AI%20Engineer%20|%20Full%20Stack%20Developer%20|%20Builder&descAlign=50&descAlignY=60&descColor=D6F0FF)

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=30&duration=2800&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&height=60&lines=Building+Production+Systems;AI+Engineering+%26+Backend+Architecture" />
</p>

<p align="center">
  <b>Information Science & Engineering</b> at <b>The National Institute of Engineering, Mysuru</b> (2024-2028)<br/>
  Engineering real-world systems with depth in distributed backends, AI integration, and real-time architectures.
</p>

<p align="center">
  <a href="https://www.vansh917.me"><img src="https://img.shields.io/badge/Portfolio-vansh917.me-000000?style=flat-square&logo=vercel&logoColor=white"/></a>
  <a href="https://linkedin.com/in/vansh917"><img src="https://img.shields.io/badge/LinkedIn-vansh917-0077B5?style=flat-square&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:vanshg917@gmail.com"><img src="https://img.shields.io/badge/Email-vanshg917@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white"/></a>
  <a href="https://instagram.com/vansh___917"><img src="https://img.shields.io/badge/Instagram-@vansh___917-E4405F?style=flat-square&logo=instagram&logoColor=white"/></a>
</p>

---

## Featured Systems

### [NIEdge](https://niedge.vercel.app) - Student Academic Resource Platform
- **Impact:** 1,700+ total users and 32,000+ views across student academic workflows.
- **Architecture:** Decoupled client communicating with serverless Cloudflare Workers acting as low-latency API routing gateways and Cheerio-based scrapers.
- **Reliability:** Offline-first PWA with Service Worker asset caching and a sandboxed browser development playground.
- **Tech Stack:** JavaScript, Cloudflare Workers, Firebase, Service Workers, Cheerio.

### [AlphaEngineX](https://alphaenginex.vercel.app) - Algorithmic Market Simulator
- **Architecture:** Layered Flask backend (`routes` -> `services` -> `repositories`) backed by a 7-collection MongoDB production schema.
- **Concurrency & Safety:** Atomic MongoDB transactions (`$inc`, `$push`) with UUIDv4 idempotency for race-condition-safe order execution under concurrent spikes.
- **Market Dynamics:** Demand-driven volatility modeling across 15 assets with APScheduler-driven 2-second price updates, per-user rate limits, and audit trails.
- **Tech Stack:** Python, Flask, React, MongoDB Atlas, Firebase, Groq API.

### [Lumen](https://lumen.vansh917.me) - Native Desktop AI Client
- **Architecture:** Multi-process Electron application isolating privileged Node.js APIs from the renderer via a typed, Zod-validated IPC bridge.
- **State Management:** Partitioned 7-store Zustand state architecture maintaining 60 FPS UI stability during active local LLM token streaming.
- **Storage & Privacy:** Local SQLite storage in WAL mode via Drizzle ORM, zero cloud telemetry, fully offline inference via Ollama.
- **Tech Stack:** Electron, TypeScript, React, Zustand, Drizzle ORM, SQLite, Vite, Zod.

### [CrediGraph](https://credigraph.streamlit.app) - Graph-Native Risk & Fraud Intelligence
- **Modeling:** 2-layer GraphSAGE neural network (0.952 AUC-ROC) evaluating 100,000 counterparties across 4,002,354 relational exposure edges.
- **Inference Pipeline:** Soft-voting ensemble (XGBoost, Random Forest, GNN) with parallel asynchronous scoring dispatch under 150ms via ThreadPoolExecutor.
- **Tech Stack:** Python, PyTorch, PyTorch Geometric, XGBoost, Scikit-Learn, Streamlit, NetworkX.

---

## Technical Competencies

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,python,c,java,html,css,react,nextjs,vite,tailwind,nodejs,express,fastapi,flask,electron,postgres,supabase,mongodb,mysql,sqlite,redis,firebase,pytorch,cloudflare,docker,git,github,postman,vercel&perline=15&theme=dark"/>
</p>

<table align="center" width="100%">
  <tr>
    <td width="25%"><b>Languages</b></td>
    <td>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
      <img src="https://img.shields.io/badge/JavaScript-323330?style=flat-square&logo=javascript&logoColor=F7DF1E"/>
      <img src="https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54"/>
      <img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white"/>
      <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td width="25%"><b>AI & Deep Learning</b></td>
    <td>
      <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
      <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
      <img src="https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi"/>
    </td>
  </tr>
  <tr>
    <td width="25%"><b>Frontend & State</b></td>
    <td>
      <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white"/>
      <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
      <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white"/>
      <img src="https://img.shields.io/badge/Zustand-443e38?style=flat-square&logo=react&logoColor=white"/>
      <img src="https://img.shields.io/badge/Zod-3E67B1?style=flat-square&logo=zod&logoColor=white"/>
      <img src="https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white"/>
      <img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white"/>
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td width="25%"><b>Backend & Systems</b></td>
    <td>
      <img src="https://img.shields.io/badge/Node.js-6DA55F?style=flat-square&logo=node.js&logoColor=white"/>
      <img src="https://img.shields.io/badge/Express.js-404d59?style=flat-square"/>
      <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask"/>
      <img src="https://img.shields.io/badge/Electron-47848F?style=flat-square&logo=electron&logoColor=white"/>
      <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socketdotio&logoColor=white"/>
      <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td width="25%"><b>Databases & Cache</b></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white"/>
      <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white"/>
      <img src="https://img.shields.io/badge/MongoDB-4ea94b?style=flat-square&logo=mongodb&logoColor=white"/>
      <img src="https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white"/>
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
      <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black"/>
      <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td width="25%"><b>DevOps & Cloud</b></td>
    <td>
      <img src="https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white"/>
      <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white"/>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
      <img src="https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white"/>
      <img src="https://img.shields.io/badge/Git-F05033?style=flat-square&logo=git&logoColor=white"/>
      <img src="https://img.shields.io/badge/GitHub-121011?style=flat-square&logo=github&logoColor=white"/>
      <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white"/>
      <img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white"/>
      <img src="https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white"/>
    </td>
  </tr>
</table>

---

<p align="center">
  <sub>Engineered by <a href="https://www.vansh917.me">Vansh Gupta</a>. Built for scale, performance, and correctness.</sub>
</p>
