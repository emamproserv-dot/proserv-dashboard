import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# =============================
#  Load Data
# =============================
clients = pd.read_excel("data/clients.xlsx")
finance = pd.read_excel("data/finance.xlsx")

# =============================
#  Data Processing (Place all your previous data cleaning & calculations here)
#  Example: Active Clients per Year
clients["Year"] = pd.to_datetime(clients["Renewal Date"].astype(str) + "-01-01", errors="coerce").dt.year
clients_per_year = clients.groupby("Year")["Company Name"].nunique().reset_index(name="Active_Clients")

fig1 = px.bar(clients_per_year, x="Year", y="Active_Clients", text="Active_Clients", template="plotly_white")

# =============================
#  Dash App
# =============================
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Proserv Strategic & Financial Dashboard"),

    html.H2("Active Clients by Year"),
    dcc.Graph(figure=fig1),

    # أضف باقي الرسومات هنا بنفس الطريقة:
    # dcc.Graph(figure=fig2), dcc.Graph(figure=fig3), ...
])

if __name__ == "__main__":
    app.run_server(debug=True)
