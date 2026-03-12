# # GDZY_LLM: Field Deployment Records for SCOLT

This repository provides archived field data from Plant A, where the SCOLT (Semantic Control Optimization using Language Transformers) framework was deployed in 2023 on a 410 t/h pulverized coal-fired boiler. Due to cybersecurity restrictions, raw SCADA logs could not be exported; however, timestamped screenshots were captured from the operator interface to document system behavior under LLM-guided tuning.

## 📁 Repository Structure

- `data/`: Contains annotated screenshots from 24–72 hours of real-time loop operation.
  - `feedwater/`: Drum level control trends
  - `furnace_pressure/`: Negative pressure loop response
  - `coal_feed/`: Coal feed rate dynamics under ramp events
- `appendix/`: Supplementary notes on SCADA environment and constraints.

## 🕓 Observation Period

All data were captured between **2023-09-02 and 2023-09-09** (UTC+8), reflecting LLM-on operation in real production conditions. Each loop contains at least **24 hours** of continuous traceable evidence.

## 🔒 Data Ethics and Security

- All screenshots are anonymized.
- No proprietary operator data is disclosed.
- SCOLT control recommendations were visible on screen but are not reverse-engineered from the LLM model.

## 🔗 Citation

## 实现代码

SCOLT 控制器实现与算法对比实验代码：[**SCOLT**](https://github.com/Tedchai/SCOLT-Code)

