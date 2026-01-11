from flask import Flask, render_template

app = Flask(__name__)

# Dashboard pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sales-drilldown')
def sales_drilldown():
    return render_template('sales-drilldown.html')

@app.route('/geographic-drilldown')
def geographic_drilldown():
    return render_template('geographic-drilldown.html')

@app.route('/time-drilldown')
def time_drilldown():
    return render_template('time-drilldown.html')

@app.route('/user-behavior-drilldown')
def user_behavior_drilldown():
    return render_template('user-behavior-drilldown.html')

@app.route('/customer-analytics')
def customer_analytics():
    return render_template('customer-analytics.html')

@app.route('/marketing-performance')
def marketing_performance():
    return render_template('marketing-performance.html')

@app.route('/inventory-management')
def inventory_management():
    return render_template('inventory-management.html')

@app.route('/financial-overview')
def financial_overview():
    return render_template('financial-overview.html')

@app.route('/product-analytics')
def product_analytics():
    return render_template('product-analytics.html')

@app.route('/product-hierarchy-drilldown')
def product_hierarchy_drilldown():
    return render_template('product-hierarchy-drilldown.html')

# Chart tutorial pages
@app.route('/bar-column-charts')
def bar_column_charts():
    return render_template('tutorials/bar-column-charts.html')

@app.route('/line-area-charts')
def line_area_charts():
    return render_template('tutorials/line-area-charts.html')

@app.route('/pie-donut-charts')
def pie_donut_charts():
    return render_template('tutorials/pie-donut-charts.html')

@app.route('/scatter-bubble-charts')
def scatter_bubble_charts():
    return render_template('tutorials/scatter-bubble-charts.html')

@app.route('/heatmap-treemap-charts')
def heatmap_treemap_charts():
    return render_template('tutorials/heatmap-treemap-charts.html')

@app.route('/radar-polar-charts')
def radar_polar_charts():
    return render_template('tutorials/radar-polar-charts.html')

# Bootstrap component tutorial pages
@app.route('/layout-components')
def layout_components():
    return render_template('tutorials/layout-components.html')

@app.route('/navigation-elements')
def navigation_elements():
    return render_template('tutorials/navigation-elements.html')

@app.route('/forms-inputs')
def forms_inputs():
    return render_template('tutorials/forms-inputs.html')

@app.route('/cards-modals')
def cards_modals():
    return render_template('tutorials/cards-modals.html')

@app.route('/tables-data-display')
def tables_data_display():
    return render_template('tutorials/tables-data-display.html')

@app.route('/responsive-design')
def responsive_design():
    return render_template('tutorials/responsive-design.html')

if __name__ == '__main__':
    app.run(debug=True)
