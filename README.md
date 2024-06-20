<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="850"
        src="https://media.roboflow.com/open-source/autodistill/autodistill-banner.png?3"
      >
    </a>
  </p>
</div>

# Autodistill Target Model Template

**⚠️ Note: Before you start building a Target Model, check out our [Supported Models](https://docs.autodistill.com/supported-models/) documentation to see if a model is already being implemented. If your desired model is being implemented, check the [Autodistill](https://github.com/autodistill/autodistill) GitHub Issues for progress. We encourage you to offer support to models you want to see in Autodistill if work is already being done on them.**

This repository contains a template for use in creating a Target Model for [Autodistill](https://github.com/autodistill/autodistill).

Autodistill works with two categories of model:

1. A Base Model. This is a large model that knows (or combination of models that know) how to identify many different objects.
2. A Target Model. This is a model architecture on which you can train a smaller model using labeled data from the Base Model.

Autodistill is an ecosystem of Base and Target Models, with the main [Autodistill](https://github.com/autodistill/autodistill) repository acting as the bridge between the two.

This repository contains a starter template from which you can create a Target Model extension.

Read the full [Autodistill documentation](https://autodistill.github.io/autodistill/).
## Steps to Build a Target Model

To build a target model, first rename the `autodistill_target_model` directory to the name of the model you want to implement:

```
autodistill_model_name
```

Use underscores to separate words in the folder name.

Next, open the `model.py` file. This is the file where your model loading and inference code will be stored. If you need to write helper functions for use with your model -- for example, long methods for loading data, processing extensions -- you may opt to create new files to store the helper scripts.

In `model.py`, replace the `Model` class name with the name of your model.

Next, implement the following functions:

1. `__init__`: Code for loading the model.
2. `predict`: A function that takes in an image name, runs inference, and returns a `supervision` Detections object (object detection) or a `supervision` Classifications object (classification).
3. `train`: A function that takes a dataset and trains a model. For object detection, we prefer YOLOv5 PyTorch TXT if possible. For classification, we prefer Classification Folder structure.

Replace the import statement in the `__init__.py` file in your model directory to point to your model. You only need to import the model, such as:

```
from autodistill_yolov5.model import YOLOv5
```

Your version should be set in the `__init__.py` file as `0.1.0` before submitting your model for review.

Update the `setup.py` file to use the name of your model where appropriate. Add all of the requisite dependencies to the `install_requires` section.

Your Target Model must feature a README that shows a minimal example of how to use the model. This should only be a few lines of code. Refer to `README_EXAMPLE.md` for an example of an Autodistill Target Model README. Feel free to copy this example and replace all parts as required.

Your package must be licensed under the same license as the model you are using (i.e. if your model uses an Apache 2.0 license, your Autodistill extension must use the same license). Your license should be in a file called `LICENSE`, stored in the root directory of your Autodistill extension GitHub repository.

Update your README to note the license applied to your package.

When your Autodistill extension is ready for testing, open an Issue in the main [Autodistill](https://github.com/autodistill/autodistill) repository with a link to a public GitHub repository that contains your code.

An Autodistill maintainer will review your code. If accepted, we will:

1. Add your package to the [Autodistill documentation](https://docs.autodistill.com).
2. Package your project up to PyPi and publish it as an official `autodistill` extension.
3. Announce your project on social media.
