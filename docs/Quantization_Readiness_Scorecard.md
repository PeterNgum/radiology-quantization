# Quantization Readiness Scorecard for Radiology AI Models

This scorecard provides a framework to assess if a radiology AI model is suitable for quantization and identify key considerations.

**Model Details:**
- Model Name/Version:
- Task:
- Original Performance Metric(s) & Value(s):
- Target Deployment Environment (Cloud, On-Prem Server, Edge Device, Mobile):

**Assessment Criteria:**

| Category             | Question                                                                        | Score (1-5) | Notes / Mitigation                                       |
| :------------------- | :------------------------------------------------------------------------------ | :---------- | :------------------------------------------------------- |
| **Performance**      | How sensitive is the model's key performance metric to numerical precision?      |             | *Initial PTQ test, literature review*                    |
|                      | Is there an acceptable performance drop tolerance defined for clinical use?     |             | *+/- X% AUC/Dice, Consult clinicians*                   |
| **Data**             | Is a representative calibration dataset available for PTQ?                      |             | *Subset of validation data*                              |
|                      | Are there known data shifts or outlier populations in the target deployment?   |             | *Robustness testing needed post-quantization*          |
| **Deployment**       | What are the primary computational constraints (Memory, Latency, Power)?         |             | *Target hardware specs*                                |
|                      | Does the target hardware have optimized support for INT8/INT4 inference?        |             | *CPU (AVX), GPU (Tensor Cores), Edge TPU/NPU*          |
| **Validation**       | How will the quantized model's performance be validated clinically?              |             | *Prospective study, shadow mode, reader study*         |
|                      | Are there regulatory requirements (e.g., FDA/MDR) for re-validating the model? |             | *Documentation, traceability*                          |
| **Effort**           | How complex is integrating quantization (PTQ vs. QAT)?                          |             | *PTQ simpler, QAT requires retraining infrastructure* |
|                      | Are the necessary tools/libraries compatible with the model framework?          |             | *PyTorch Quantization, TFLite Converter, bitsandbytes* |

**Scoring Guide:**
- 5: Highly Ready / Low Risk
- 3: Moderately Ready / Manageable Risk
- 1: Low Readiness / High Risk / Significant Effort Needed

**Overall Readiness Score:** [Sum Scores] / 50 = **XX.X%**

**Recommendation:** (e.g., Proceed with PTQ, Consider QAT, Further investigation needed)

**Key Risks/Considerations:**
- [Risk 1]
- [Risk 2]

*This scorecard is a guide; clinical and technical expertise is required for final decisions.*
