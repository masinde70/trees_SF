
---

# SF Trees Analysis App

This project is an interactive dashboard built with Streamlit for analyzing tree data in San Francisco. The dashboard allows users to visualize and filter information about trees, such as their width and age, using a dataset provided by the San Francisco Department of Public Works (SF DPW).

## Features

- **Interactive Filtering:** Filter trees by their caretaker/owner using a sidebar.
- **Customizable Visualizations:** Change the color of the histogram charts using a color picker.
- **Tree Width Distribution:** View the distribution of tree trunk diameters (DBH).
- **Tree Age Distribution:** View the distribution of tree ages (in days).
- **Responsive Layout:** Two side-by-side charts for easy comparison.

## How it Works

- Loads a CSV file (`trees.csv`) containing tree data.
- Calculates the age of each tree based on the planting date.
- Allows users to filter trees by owner and select custom colors for plots.
- Visualizes tree width and age using histograms.

## Getting Started

### Prerequisites

- Python 3.7+
- Required Python packages: `pandas`, `plotly`, `streamlit`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/masinde70/trees_SF.git
    cd trees_SF
    ```

2. Install dependencies:
    ```bash
    pip install pandas plotly streamlit
    ```

3. Place your `trees.csv` data file in the project directory.

### Running the App

```bash
streamlit run pretty_trees.py
```

Open the web browser at the URL provided by Streamlit to use the dashboard.

## Dataset

- The app expects a `trees.csv` file with at least the following columns: `tree_id`, `dbh` (diameter at breast height), `date` (planting date), and `caretaker` (tree owner).

## License

This project is provided for educational and analytical purposes.

---

