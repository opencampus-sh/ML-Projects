---
marp: true
theme: gaia
size: 4:2
_class: lead
paginate: true
backgroundColor: lightgray
backgroundImage: url('./cover.jpg')
---


# **A Neural Style Transfer**

[[Paper](https://arxiv.org/pdf/1508.06576.pdf)]

---

# :bookmark_tabs: **Contents**

- Introduction
- Architecture
- Optimization
- Results / Implementation

---

# Introduction

- Extension of Texture transfer
- Pre-Trained Feature Extraction Architectures [ CNNs ]
- Reconstructed from different layer responses
- Content and Style Reconstruction Loss

---

# Architecture

![bg 60%](./vgg19.png)

---

![bg 65%](./architecture.png)

---

# Optimization


$$
\boxed{
    \mathscr{L_{total} (\vec{p}, \vec{a}, \vec{x})} = 
        \alpha \mathscr{L_{content}}(\vec{p}, \vec{x}) + 
        \beta \mathscr{L_{style}}(\vec{a}, \vec{x})
}
$$

$$

    \mathscr{L}_{content}(\overrightarrow{p}, \overrightarrow{x}, l) =
    \frac{1}{2} \sum( F^{l} _{ij} - P^{l} _{ij})^2 

$$

$$

    \mathscr{L}_{style}(\vec{a},\vec{x}) = \sum_{l=0}^{l}w_lE_l

$$


---

![bg 80%](./optimization.jpg)



---

# Results / Implementation
[[Here](https://github.com/Mnpr/Art-Generation-GANs/tree/main/src/style_based_generation)]

![bg 78%](./styles.png)

![bg 90%](./results.png)




