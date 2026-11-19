# Does AI Confidence Behave Like Probability?

Testing whether an AI model's stated confidence predicts the correctness of its medical multiple-choice answers.

## Research question

Does an AI model's stated confidence correspond to the actual probability that its selected answer is correct?

## Experiment

- 200 four-option medical examination questions from MedQA-USMLE.
- 150 questions used as a development set.
- 50 questions held out as a locked test set.
- The same visible ChatGPT model selection and response prompt were used across batches.
- Test responses were collected in fresh conversations from a separate ChatGPT account without previous conversation context.
- The exact underlying model version was not independently recorded.
- The model returned one answer choice and a confidence percentage for each question.

The experiment was designed to study calibration, not to build a new predictive model.

## Evaluation

For each answer, confidence was converted to a probability p and correctness was represented by y ∈ {0,1}.

The project uses accuracy, mean confidence, Brier score, calibration curves, and Expected Calibration Error (ECE).

## Results

| Metric | Development (150) | Locked test (50) |
|---|---:|---:|
| Accuracy | 89.33% | 92.00% |
| Mean confidence | 98.14% | 95.78% |
| Brier score | 0.0986 | 0.0604 |
| ECE | 8.99% | 6.26% |

The development set contained 134 correct and 16 incorrect answers. The locked test contained 46 correct and 4 incorrect answers.

## Limitations

Some questions referenced visual materials, such as a peripheral blood smear or a graph, that were not included in the text-only prompts. This may have affected answerability for those items.

MedQA is publicly available and the model's training data are unknown, so prior exposure to some benchmark questions cannot be ruled out.

The locked test contains only 50 questions, so its accuracy and calibration estimates are uncertain and should not be generalized broadly.

No prediction received exactly 100% confidence, so the specific hypothesis that a 100% confidence prediction would always be correct could not be directly tested.

## Public repository contents

This public repository contains the final report, thumbnail, calibration visualization, and aggregated calibration data. The raw locked answer key and individual model-response files are intentionally not published.

## References

Jin, D., Pan, E., Oufattole, N., Weng, W.-H., Fang, H., & Szolovits, P. (2021). *What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams*. Applied Sciences, 11(14), 6421.

Dataset: https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options

## AI use disclosure

AI tools were used to help refine the research question, generate model predictions, develop and debug Python scripts, produce the calibration visualization, create the thumbnail artwork, organize the evaluation, and structure the report. The student selected and prepared the dataset, organized and ran the experiment, collected the responses, reviewed the outputs, and made the final analytical decisions and conclusions.
