# Field Disclosure Note for SCOLT Deployment (Plant A)

This disclosure summarizes constraints and scope related to the field deployment of SCOLT (Semantic Control Optimization using Language Transformers) on Boiler Unit #5 at Plant A in 2023.

## 🔐 Export Restrictions

Due to strict cybersecurity and data confidentiality protocols at the plant site:

- **Raw SCADA logs and DCS exports could not be obtained or published.**
- Control loop logs were viewed via a secure monitoring terminal with no remote export access.
- Only timestamped **screenshots** and **Excel calibration tables** could be captured during on-site sessions.

## 📸 Dataset Representation

Instead of log files, the dataset includes:

- Annotated trend screenshots for feedwater and furnace pressure (pre/post SCOLT tuning).
- An Excel table capturing actuator behavior for coal feed loop tuning.
- Metadata files documenting loop configuration, timestamps, and test conditions.

Each record reflects **at least 24 hours** of traceable loop operation and tuning activity.

## 🧠 SCOLT Visibility

The SCOLT framework was deployed in real-time and interfaced with the DCS/SCADA operator station:

- LLM-tuned PID suggestions were **visible on screen**.
- Operator accepted/rejected actions were manually verified.
- The inference backend was not exported or reverse-engineered.

## 📝 Reuse and Citation

These records are made publicly available to support academic reproducibility and model evaluation.  
If used in research, please cite the associated BuildSys2025 paper:

> Author(s). *Energy-Efficient Modular Control and Optimization for Pulverized Coal-Fired Boiler Systems in Industrial Plants*. BuildSys 2025.

Repository: [https://github.com/Tedchai/GDZY_LLM](https://github.com/Tedchai/GDZY_LLM)
