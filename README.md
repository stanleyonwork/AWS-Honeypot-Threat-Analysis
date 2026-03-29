# AWS Honeypot Threat Analysis
![BI Dashboard Preview 1](./Dashboard/dashboard_preview_1.png)
![BI Dashboard Preview 2](./Dashboard/dashboard_preview_2.png)
![BI Dashboard Preview 3](./Dashboard/dashboard_preview_3.png)

**Lead Architect:** Gading Mahendra Sebayang
**Target:** 448K+ AWS Honeypot Log Entry
**Core Stack:** Python (Pandas) | Power BI

---

### ⚡ Technical Specifications
| Component | Implementation |
| :--- | :--- |
| **Pipeline** | End-to-End ETL (01_EDA -> 02_Cleaning) |
| **Data Architecture** | One Big Table (OBT) for high-speed indexing |
| **Memory Opt.** | Columnar compression via VertiPaq engine |
| **Security Scope** | Threat Intelligence & Geospatial SOC Simulation |

### 📂 Repository Structure
* `data/`: Raw & Cleaned OBT datasets (`.csv`)
* `scripts/`: Python Pandas ETL logic
* `Dashboard/`: `.pbix` source & visual rendering

### 🛡️ Backend Architecture (Python)
1.  **Exploration (`01_honeypot_eda.py`):** Schema diagnostics & null-value mapping.
2.  **Transformation (`02_data_cleaning_obt.py`):** * Dropping residual telemetry (`Unnamed: 15`).
    * Standardizing protocols (Port 0 assignment for ICMP).
    * ISO-8601 Timestamp casting & semantic renaming.

### 📊 Visualization Logic
Rendering 448,000+ spatial nodes directly from memory to bypass browser-based DOM lag.
* **Intelligence Metrics:** Attack frequency, port vulnerability matrix, and attacker geolocation.
* **Operational Status:** Local execution recommended via `.pbix` for full VertiPaq interactivity.