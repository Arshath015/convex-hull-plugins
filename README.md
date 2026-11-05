Convex Hull via Graham Scan Algorithm
===========================

[![Python Version](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)

One-line pitch: A plugin-based implementation of the Graham scan algorithm for calculating the convex hull of a set of points.

## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Case Study](#case-study)
* [Testing](#testing)
* [Limitations](#limitations)
* [Roadmap](#roadmap)
* [License](#license)

## Overview
This project provides a plugin-based implementation of the Graham scan algorithm for calculating the convex hull of a set of points.

## Tech Stack
* Python 3.x
* NumPy

## Architecture
```
plugins/
  basic_plugin.py
  optimized_plugin.py
core/
  registry.py
tests/
  test_basic_plugin.py
  test_optimized_plugin.py
examples/
  demo.py
docs/
  case_study.md
```
## Theoretical Background
The convex hull of a set of points is the smallest convex polygon that contains all the points. The Graham scan algorithm is a popular method for calculating the convex hull. This algorithm has a time complexity of O(n log n) and a space complexity of O(n).

The Graham scan algorithm works by first finding the leftmost point and then sorting the remaining points based on their polar angles with respect to the leftmost point. It then iterates through the sorted points and adds them to the convex hull if they make a left turn with respect to the previous two points.

## Installation
To install this project, run the following commands:
```bash
pip install -r requirements.txt
git clone https://github.com/username/convex-hull-plugins.git
```
## Usage
To use this project, simply run the demo.py script in the examples directory:
```bash
python examples/demo.py
```
## API Reference
The API reference for this project is as follows:
* `BasicPlugin.convex_hull(points)`: calculates the convex hull of a set of points using the Graham scan algorithm
* `OptimizedPlugin.convex_hull(points)`: calculates the convex hull of a set of points using an optimized version of the Graham scan algorithm

## Case Study
For a case study on this project, please see [docs/case_study.md](docs/case_study.md)

## Testing
To run the tests for this project, simply run the following command:
```bash
pytest tests/
```
## Limitations
The current implementation of this project has the following limitations:
* It only supports 2D points
* It does not handle degenerate cases (e.g. collinear points)

## Roadmap
The roadmap for this project is as follows:
* Add support for 3D points
* Handle degenerate cases (e.g. collinear points)

## License
This project is licensed under the MIT license.

## Requirements

```
pip install -r requirements.txt
```


---
**Last updated:** 2026-11-05
