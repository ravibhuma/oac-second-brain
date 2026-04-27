# Machine Learning & AI Features

> **Last updated:** 2026-04-27
> **Tags:** machine learning, AI, OML, AutoML, explain, natural language, AI assistant, augmented analytics, clustering, regression, classification

## Summary
OAC integrates machine learning and AI capabilities at multiple levels: automated insight discovery (Explain), natural language querying (Ask), generative AI (AI Assistant), in-platform model training (OML via Data Flows), and OCI AI Services integration (Vision, Language, Forecasting). These features make analytics accessible to both business users and data scientists.

---

## Augmented Analytics (Business User AI)

### Explain
Automatically analyzes a selected measure and generates insight visualizations:

**Access**: Right-click a column in a Workbook → **Explain**

**Generated Insight Types**:
| Insight | What It Shows |
|---|---|
| **Basic Facts** | Distribution, total, average, nulls |
| **Key Drivers** | Which dimensions have the highest correlation with the measure |
| **Segments** | Clusters of data points with similar behavior |
| **Anomalies** | Outliers and unexpected values |

Each insight is presented as a visualization; users can **add to canvas** with one click.

### Ask (Natural Language Query)
Type plain English questions to generate visualizations:

**Access**: Workbook → **Ask** bar (top of canvas)

**Examples**:
```
"Show revenue by region for 2024"
"Top 10 products by profit margin"
"Compare sales this year vs last year"
"What is the trend for customer count?"
```

OAC interprets the question, selects appropriate columns, and renders a visualization. Users can then adjust or refine.

### Auto Insights
OAC proactively surfaces insights when opening a Workbook:
- Identifies metrics that changed significantly
- Detects correlations
- Surfaces anomalies
Access: **View** → **Auto Insights** panel

### AI Assistant (Generative AI)
Powered by OCI Generative AI Services:
- **Describe**: Generate a natural language description of a visualization
- **Ask questions**: Conversational Q&A against the dataset
- **Suggest**: Recommend visualization types for your data
- **Code generation**: Generate Logical SQL from a description

**Setup**: Enable in Service Console → AI & Machine Learning → Configure OCI GenAI connection

---

## Oracle Machine Learning (OML) in Data Flows

Train and apply ML models using a visual pipeline — no coding required.

### Supported Algorithm Categories

**Numeric Prediction (Regression)**
| Algorithm | Best For |
|---|---|
| Linear Regression | Linear relationships |
| Random Forest Regression | Non-linear, high dimensionality |
| Gradient Boosting Regression | High accuracy, tabular data |
| Neural Network Regression | Complex patterns |

**Binary Classification**
| Algorithm | Best For |
|---|---|
| Logistic Regression | Interpretable, linear boundary |
| Random Forest Classifier | Balanced accuracy |
| Gradient Boosting Classifier | High accuracy |
| SVM (Support Vector Machine) | High-dimensional |
| Naïve Bayes | Text, categorical features |

**Multi-Class Classification**
Same algorithms as binary, extended to multiple classes.

**Clustering**
| Algorithm | Best For |
|---|---|
| K-Means | Known number of clusters |
| Hierarchical Clustering | Exploring cluster structure |

### Training a Model (Data Flow)

1. Create a Data Flow
2. Add **Train Numeric Prediction** (or other train step)
3. Configure:
   - **Target column**: what you're predicting
   - **Input columns**: features
   - **Algorithm**: auto or specific
   - **Model name**: saved to Models catalog
4. Run the Data Flow
5. View model quality metrics (RMSE, accuracy, AUC, etc.)

### Applying a Model (Scoring)

1. Create a Data Flow
2. Add your data source
3. Add **Apply Model** step → select trained model
4. Output includes prediction column + probability/confidence
5. Save as Dataset for visualization

---

## OCI AI Services Integration

OAC can call Oracle Cloud AI Services from within Data Flows.

### Oracle AI Vision (Image Analysis)
- Object detection, image classification, custom model
- **Use case**: Analyze product images, detect defects in IoT images

### Oracle AI Language
- Sentiment analysis on text columns
- Key phrase extraction
- Named entity recognition (NER)
- Language detection
- Text classification

**Data Flow Step**: Add **System Connection** → select OCI Language Service → select operation

### Oracle AI Forecasting
- Time-series forecasting service
- Predicts future values of metrics
- **Use case**: Revenue forecasting, demand planning, inventory prediction

### Oracle AI Document Understanding
- Extract text from PDFs and images (OCR)
- Table extraction from scanned documents
- Key-value pair extraction

---

## Pre-Built Models vs. Custom Models

| Scenario | Approach |
|---|---|
| Standard prediction task (regression/classification) | Train via Data Flow (OML) |
| Complex custom model | Train in OCI Data Science → register in OAC |
| Text/image analysis | OCI AI Language / Vision service |
| Time-series forecasting | OCI AI Forecasting service |

---

## Registering External Models (OCI Data Science)

Models trained in OCI Data Science (Python, AutoML) can be registered in OAC:
1. Save model to OCI Model Catalog
2. OAC → **Machine Learning** → **Register** → point to OCI Model Catalog entry
3. Apply registered model in a Data Flow **Apply Model** step

---

## Model Management

**Home** → **Machine Learning** (navigation item):
- View all trained models
- Model quality metrics
- Related Data Flows
- Delete or rename models

---

## Best Practices

> 💡 Tip: Use Explain on your key business metrics to quickly discover which dimensions are driving changes — no ML expertise needed.

> 💡 Tip: Always evaluate model quality metrics before deploying predictions. For regression: RMSE, R²; for classification: accuracy, AUC, precision/recall.

> ⚠️ Warning: OML models trained in Data Flows use OAC's in-memory engine. For production-grade models on large data, use OCI Data Science and register the model.

> 💡 Tip: Apply Model outputs a prediction score. Join this back to your visualization dataset to show predictions alongside actuals.

---

## Related
- [[Data Flows & Data Preparation]]
- [[Workbooks & Visualizations]]
- [[Subject Areas & Datasets]]
- [[APIs, Embedding & Integration]]
