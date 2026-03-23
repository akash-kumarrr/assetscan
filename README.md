<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=F59E0B&height=220&section=header&text=AssetScan&fontSize=90&fontColor=ffffff&animation=fadeIn&fontAlignY=40&desc=IT%20Asset%20Management%20%E2%80%94%20Scan.%20Verify.%20Act.&descAlignY=60&descColor=1a1a1a&descSize=20" width="100%"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=F59E0B&center=true&vCenter=true&width=620&lines=QR-Powered+IT+Asset+Management+%F0%9F%93%A6;Real-Time+Hardware+Tracking+%F0%9F%9F%A2;Built+with+FastAPI+%2B+Flutter+%E2%9A%A1;Scan+%E2%86%92+Verify+%E2%86%92+Act)](https://readme-typing-svg.demolab.com)

<br/>

![Python](https://img.shields.io/badge/Python_3.11+-F59E0B?style=for-the-badge&logo=python&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

<br/>

![License](https://img.shields.io/badge/License-MIT-22D3EE?style=flat-square)
&nbsp;
![Version](https://img.shields.io/badge/Version-1.0.0-4ADE80?style=flat-square)
&nbsp;
![Status](https://img.shields.io/badge/Status-Active-F59E0B?style=flat-square)
&nbsp;
![Platform](https://img.shields.io/badge/Platform-Mobile%20%2B%20Web-F87171?style=flat-square)

</div>

<br/>

---

## 🔍 What is AssetScan?

> **AssetScan** is a professional IT asset management utility that bridges the gap between physical hardware and digital records using high-speed QR technology.

Built for organizations that need to **track, assign, and audit physical hardware at scale** — with a Flutter mobile app for field staff and a web dashboard for administrators, all powered by a FastAPI + PostgreSQL backend.

<br/>

---

## ✨ Features

<div align="center">

| | Feature | Description |
|:---:|:---|:---|
| 📷 | **QR Identification** | Instantly identify Laptops, Monitors & Servers via unique QR codes |
| 🔄 | **Dynamic Assignment** | Check-out to employees or check-in to warehouse in one tap |
| 🟢 | **Real-Time Status** | Track `Available` · `Assigned` · `Under Repair` across your org |
| 📋 | **Ownership History** | Full audit trail of every user who handled an asset |
| 📱 | **Mobile App** | Flutter app optimized for high-speed camera scanning in the field |
| 🖥️ | **Web Dashboard** | Admin interface for bulk management and data entry |

</div>

<br/>

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,fastapi,flutter,dart,postgres,docker&theme=dark" />

<br/><br/>

| Layer | Technology | Purpose |
|:---:|:---|:---|
| 🐍 **Backend** | Python 3.11+ · FastAPI | REST API, QR generation, business logic |
| 🎯 **Frontend** | Dart · Flutter | Mobile scanner app + Web admin dashboard |
| 🗄️ **Database** | PostgreSQL 15+ | Asset records, transaction history |
| 🐳 **DevOps** | Docker · Docker Compose | Containerized deployment |

</div>

<br/>

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/akash-kumarrr/assetscan.git
cd assetscan

# 2. Start all services with Docker
docker compose up --build

# 3. Open the web dashboard
open http://localhost:8000

# 4. Run the Flutter mobile app
cd mobile && flutter run
```

<br/>

---

## 📁 Project Structure

```
assetscan/
├── 📂 backend/
│   ├── main.py              # FastAPI entry point
│   ├── models/              # SQLAlchemy models
│   ├── routes/              # API route handlers
│   └── qr/                  # QR generation logic
├── 📂 mobile/               # Flutter mobile app (scanner)
├── 📂 web/                  # Flutter web dashboard (admin)
├── 🐳 docker-compose.yml
└── 📄 README.md
```

<br/>

---

## 🔴 Asset Status Reference

<div align="center">

| Badge | Status | Meaning |
|:---:|:---:|:---|
| 🟢 | `Available` | In warehouse, ready to be assigned |
| 🟡 | `Assigned` | Checked out to an employee |
| 🔴 | `Under Repair` | Flagged for maintenance, out of service |

</div>

<br/>

---

## 👨‍💻 Developer

<div align="center">

<a href="https://github.com/akash-kumarrr">
  <img src="https://github-readme-stats.vercel.app/api?username=akash-kumarrr&show_icons=true&theme=github_dark&title_color=F59E0B&icon_color=F59E0B&border_color=30363d&bg_color=0d1117&hide_border=false" height="160"/>
  &nbsp;&nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=akash-kumarrr&layout=compact&theme=github_dark&title_color=F59E0B&border_color=30363d&bg_color=0d1117" height="160"/>
</a>

<br/><br/>

**Akash Kumar** &nbsp;·&nbsp; [`@akash-kumarrr`](https://github.com/akash-kumarrr) &nbsp;·&nbsp; `v1.0.0` &nbsp;·&nbsp; MIT License

*Free to use, modify, and distribute for personal and commercial purposes.*

</div>

<br/>

---

<div align="center">

*If you found this project helpful, please consider giving it a ⭐*

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=F59E0B&height=120&section=footer" width="100%"/>
