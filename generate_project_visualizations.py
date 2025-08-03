#!/usr/bin/env python3
"""
SpaceX Project Analysis - Visual Summary Generator
Creates comprehensive visualizations summarizing the entire project
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Set style for professional visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def create_project_overview_diagram():
    """Create a visual overview of the entire SpaceX project pipeline"""
    
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    
    # Define pipeline stages
    stages = [
        ("Data Collection", ["SpaceX API", "Web Scraping"], "#FF6B6B"),
        ("Data Processing", ["Data Wrangling", "Feature Engineering"], "#4ECDC4"),
        ("Analysis", ["EDA Visualization", "SQL Analysis"], "#45B7D1"),
        ("Geospatial", ["Folium Maps", "Location Analysis"], "#96CEB4"),
        ("Interactive", ["Dash Dashboard", "Real-time Analysis"], "#FFEAA7"),
        ("ML Modeling", ["Prediction Models", "Performance Evaluation"], "#DDA0DD")
    ]
    
    # Create pipeline visualization
    y_positions = np.linspace(0.8, 0.1, len(stages))
    
    for i, (stage_name, components, color) in enumerate(stages):
        y = y_positions[i]
        
        # Main stage box
        rect = Rectangle((0.1, y-0.05), 0.8, 0.08, 
                        facecolor=color, alpha=0.7, edgecolor='black')
        ax.add_patch(rect)
        
        # Stage title
        ax.text(0.5, y, stage_name, ha='center', va='center', 
                fontsize=14, fontweight='bold', color='white')
        
        # Components
        for j, component in enumerate(components):
            ax.text(0.05 + j*0.45, y-0.02, f"• {component}", 
                   fontsize=10, ha='left', va='center')
    
    # Add arrows between stages
    for i in range(len(stages)-1):
        y_start = y_positions[i] - 0.05
        y_end = y_positions[i+1] + 0.05
        ax.annotate('', xy=(0.5, y_end), xytext=(0.5, y_start),
                   arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    
    # Title and formatting
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('SpaceX Falcon 9 Landing Prediction - Complete Project Pipeline', 
                 fontsize=18, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('spacex_project_overview.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_notebook_analysis_chart():
    """Create a chart showing notebook analysis breakdown"""
    
    # Notebook data
    notebooks = [
        "1. SpaceX API", "2. Web Scraping", "3. Data Wrangling",
        "4. EDA Visualization", "5. EDA SQL", "6. Folium Maps", 
        "8. ML Prediction"
    ]
    
    cells = [80, 58, 56, 64, 39, 85, 87]
    focus_areas = ["Data Collection", "Data Acquisition", "Preprocessing", 
                   "Visual Analysis", "Database Analysis", "Geospatial", "Modeling"]
    
    # Create subplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Bar chart of cell counts
    colors = plt.cm.Set3(np.linspace(0, 1, len(notebooks)))
    bars = ax1.bar(range(len(notebooks)), cells, color=colors)
    ax1.set_xlabel('Notebooks', fontsize=12)
    ax1.set_ylabel('Number of Cells', fontsize=12)
    ax1.set_title('Notebook Complexity Analysis', fontsize=14, fontweight='bold')
    ax1.set_xticks(range(len(notebooks)))
    ax1.set_xticklabels([f"NB{i+1}" for i in range(len(notebooks))], rotation=45)
    
    # Add value labels on bars
    for bar, cell_count in zip(bars, cells):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{cell_count}', ha='center', va='bottom', fontsize=10)
    
    # Pie chart of focus areas
    focus_counts = {}
    for area in focus_areas:
        focus_counts[area] = focus_counts.get(area, 0) + 1
    
    # Aggregate similar areas
    analysis_distribution = {
        "Data Collection & Acquisition": 2,
        "Data Processing & Analysis": 3,
        "Visualization & Mapping": 1,
        "Machine Learning": 1
    }
    
    wedges, texts, autotexts = ax2.pie(analysis_distribution.values(), 
                                      labels=analysis_distribution.keys(),
                                      autopct='%1.1f%%', startangle=90,
                                      colors=['#FF9999', '#66B2FF', '#99FF99', '#FFD700'])
    ax2.set_title('Project Focus Distribution', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('notebook_analysis_breakdown.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_methodology_summary():
    """Create a methodology summary visualization"""
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Define methodology components
    methodologies = {
        "Data Science Lifecycle": {
            "Collection": ["REST API Integration", "Web Scraping", "Multiple Data Sources"],
            "Processing": ["Data Cleaning", "Feature Engineering", "Missing Value Handling"],
            "Analysis": ["Statistical Analysis", "Visual Analytics", "SQL Queries"],
            "Modeling": ["Machine Learning", "Cross-Validation", "Performance Metrics"],
            "Deployment": ["Interactive Dashboard", "Real-time Visualization", "User Interface"]
        }
    }
    
    # Create circular methodology diagram
    center = (0.5, 0.5)
    radius = 0.35
    
    phases = list(methodologies["Data Science Lifecycle"].keys())
    angles = np.linspace(0, 2*np.pi, len(phases), endpoint=False)
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    
    for i, (phase, angle, color) in enumerate(zip(phases, angles, colors)):
        # Calculate position
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        
        # Phase circle
        circle = plt.Circle((x, y), 0.08, color=color, alpha=0.8)
        ax.add_patch(circle)
        
        # Phase label
        ax.text(x, y, phase, ha='center', va='center', 
                fontsize=10, fontweight='bold', wrap=True)
        
        # Connect to center
        ax.plot([center[0], x], [center[1], y], 'k--', alpha=0.3, lw=1)
        
        # Add methodology details
        details = methodologies["Data Science Lifecycle"][phase]
        for j, detail in enumerate(details):
            detail_x = x + 0.15 * np.cos(angle + (j-1)*0.3)
            detail_y = y + 0.15 * np.sin(angle + (j-1)*0.3)
            ax.text(detail_x, detail_y, f"• {detail}", fontsize=8, 
                   ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", 
                   facecolor='white', alpha=0.8))
    
    # Center title
    ax.text(center[0], center[1], 'SpaceX\nProject\nMethodology', 
            ha='center', va='center', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgray', alpha=0.8))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Comprehensive Data Science Methodology Applied', 
                 fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('spacex_methodology_summary.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_technical_stack_overview():
    """Create technical stack visualization"""
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Technical stack layers
    stack_layers = [
        ("Machine Learning", ["Scikit-learn", "Cross-validation", "Model Evaluation"], "#FF6B6B"),
        ("Visualization", ["Matplotlib", "Seaborn", "Plotly", "Folium"], "#4ECDC4"),
        ("Web Framework", ["Dash", "Interactive Components", "Real-time Updates"], "#45B7D1"),
        ("Data Processing", ["Pandas", "NumPy", "JSON", "SQL"], "#96CEB4"),
        ("Data Sources", ["SpaceX API", "Wikipedia", "REST Endpoints"], "#FFEAA7")
    ]
    
    # Create stack visualization
    y_base = 0.1
    layer_height = 0.15
    
    for i, (layer_name, technologies, color) in enumerate(stack_layers):
        y_pos = y_base + i * layer_height
        
        # Layer rectangle
        rect = Rectangle((0.1, y_pos), 0.8, layer_height-0.02, 
                        facecolor=color, alpha=0.7, edgecolor='black')
        ax.add_patch(rect)
        
        # Layer name
        ax.text(0.05, y_pos + layer_height/2, layer_name, 
                ha='right', va='center', fontsize=12, fontweight='bold')
        
        # Technologies
        tech_text = " | ".join(technologies)
        ax.text(0.5, y_pos + layer_height/2, tech_text, 
                ha='center', va='center', fontsize=10)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('SpaceX Project - Technical Stack Architecture', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('spacex_technical_stack.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Generate all visualization summaries"""
    print("🚀 Generating SpaceX Project Analysis Visualizations...")
    
    print("📊 Creating project overview diagram...")
    create_project_overview_diagram()
    
    print("📈 Creating notebook analysis chart...")
    create_notebook_analysis_chart()
    
    print("🔬 Creating methodology summary...")
    create_methodology_summary()
    
    print("🛠 Creating technical stack overview...")
    create_technical_stack_overview()
    
    print("✅ All visualizations generated successfully!")
    print("\nGenerated files:")
    print("- spacex_project_overview.png")
    print("- notebook_analysis_breakdown.png") 
    print("- spacex_methodology_summary.png")
    print("- spacex_technical_stack.png")

if __name__ == "__main__":
    main()