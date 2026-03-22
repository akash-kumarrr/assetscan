# 📦 AssetScan: IT Asset Management Tool

AssetScan is a professional utility designed to bridge the gap between physical hardware and digital records using high-speed QR technology.

---

## 🚀 Key Features

* **QR-Based Identification**: Instantly identify hardware (Laptops, Monitors, Servers) by scanning a unique QR code.
* **Dynamic Assignment**: Check-out assets to specific employees or check them back into the inventory with one tap.
* **Real-Time Status Tracking**: Monitor whether an asset is `Available`, `Assigned`, or `Under Repair` across the organization.
* **Ownership History**: Maintain a complete digital audit trail of every user who has handled a specific piece of equipment.
* **Dual-Interface Support**: 
    * **Mobile (Dart/Flutter)**: Optimized for high-speed camera scanning and field use.
    * **Web (Dart/Flutter)**: Optimized for administrative data entry and bulk asset management.

---

## ⚙️ How It Works



The tool operates on a structured **Scan-Verify-Action** cycle:

1.  **Registration**: New hardware is registered in the **PostgreSQL** database via the Web Dashboard. 
2.  **QR Generation**: The **FastAPI** backend generates a unique string for the asset, which is printed as a QR code and physically attached to the hardware.
3.  **Scanning**: A staff member uses the **Flutter** mobile app to scan the physical QR code.
4.  **Verification**: The app sends the QR data to the **FastAPI** server, which queries **PostgreSQL** to retrieve the current owner and status.
5.  **Execution**: 
    * If **Available**: The user selects an employee to "Check-Out" the item.
    * If **Assigned**: The user clicks "Check-In" to return the item to the warehouse.
6.  **Update**: The database records the transaction, and the status is updated globally in real-time.

---

## 🛠️ Tech Stack

* **Backend**: Python (FastAPI)
* **Frontend**: Flutter (Dart)
* **Database**: PostgreSQL
* **DevOps**: Docker & Docker Compose

---

## 👨‍💻 Developer Information

* **Developer**: Akash Kumar
* **Project Version**: 1.0.0
* **Github**: akash-kumarrr 

---

## 📄 License

Distributed under the **MIT License**. This allows for free use, modification, and distribution of the software for both personal and commercial purposes.