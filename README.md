# Ethical Considerations

This research utilizes publicly available, anonymized social media data for non-clinical mental health classification, adhering to established ethical guidelines for social media research . The methods and results presented are intended for research purposes only and do not constitute medical advice or diagnosis. Users should be aware that Large Language Models (LLMs) are susceptible to biases and errors, and the outputs of this system should not be used to make clinical decisions. We acknowledge the potential for harm and are committed to future work addressing bias mitigation, privacy protection, and the responsible development of LLM-based mental health analysis tools. The authors and contributors are not liable for any consequences arising from the use of this research.

# Dataset

This project utilizes the published IMHI dataset from [MentalLLaMA](https://github.com/SteveKGYang/MentalLLaMA) , which supports interpretable mental health analysis on social media using Large Language Models.


# Installation

To set up the environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

# Requirements

This application requires the following:
- `qdrant` (To have accessed to our vector database please contact {521k0126, 521k0133}@student.tdtu.edu.vn
- `Gemini API Key`
- `OpenAI API Key`
- `HuggingFace API Key with Gemma access`
Make sure to set up and configure these dependencies before running the application.


# Citation
**Reference:**

```bibtex
@article{yang2023mentalllama,
  title={MentalLLaMA: Interpretable Mental Health Analysis on Social Media with Large Language Models},
  author={Yang, Kailai and Zhang, Tianlin and Kuang, Ziyan and Xie, Qianqian and Ananiadou, Sophia},
  journal={arXiv preprint arXiv:2309.13567},
  year={2023}
}
```
```bibtex
@inproceedings{yang2023towards,
  title={Towards interpretable mental health analysis with large language models},
  author={Yang, Kailai and Ji, Shaoxiong and Zhang, Tianlin and Xie, Qianqian and Kuang, Ziyan and Ananiadou, Sophia},
  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  pages={6056--6077},
  year={2023}
}
```
