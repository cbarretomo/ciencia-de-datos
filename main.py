# Dependencies
from flask import Flask, render_template, render_template_string
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from flask import request
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_plot():
 if request.method == 'POST': 
  SexoDesc= int(request.form['SexoDesc'])
  Edad= int(request.form['Edad'])
  EstadoCivilDesc= int(request.form['EstadoCivilDesc'])
  ProfesionDesc= int(request.form['ProfesionDesc'])
  indClienteEsEmpleado= int(request.form['indClienteEsEmpleado'])
  TipoClienteDesc= int(request.form['TipoClienteDesc'])
  ValorActivos= int(request.form['ValorActivos'])
  ValorEgresos= int(request.form['ValorEgresos'])
  ValorIngresos= int(request.form['ValorIngresos'])
  ValorOtrosingresos= int(request.form['ValorOtrosingresos'])
  ValorPatrimonio= int(request.form['ValorPatrimonio'])
  TotalPasivos= int(request.form['TotalPasivos'])
  NumCreditos= int(request.form['NumCreditos'])
  SaldoCreditos= int(request.form['SaldoCreditos'])
  SaldoCarteraVencida= int(request.form['SaldoCarteraVencida'])
  NumeroTC= int(request.form['NumeroTC'])
  SaldoTC= int(request.form['SaldoTC'])
  SaldoTCVencido= int(request.form['SaldoTCVencido'])
  NumeroSobregisrosUso= int(request.form['NumeroSobregisrosUso'])
  SaldoSobregirosUso= int(request.form['SaldoSobregirosUso'])
  SaldoSobregirosVencidos= int(request.form['SaldoSobregirosVencidos'])
  NumeroCuentasAhorroActivas= int(request.form['NumeroCuentasAhorroActivas'])
  SaldoCuentasAhorroActivas= int(request.form['SaldoCuentasAhorroActivas'])
  NumeroCuentasAhorroInactivas= int(request.form['NumeroCuentasAhorroInactivas'])
  SaldoCuentasAhorroInactivas= int(request.form['SaldoCuentasAhorroInactivas'])
  NumeroCuentasCorrienteActivas= int(request.form['NumeroCuentasCorrienteActivas'])
  SaldoCuentasCorrienteActivas= int(request.form['SaldoCuentasCorrienteActivas'])
  NumeroCuentascorrienteInactivas= int(request.form['NumeroCuentascorrienteInactivas'])
  SaldoCuentascorrienteInactivas= int(request.form['SaldoCuentascorrienteInactivas'])
  NumeroCDT= int(request.form['NumeroCDT'])
  SaldoCDT= int(request.form['SaldoCDT'])
  NumeroCDAT= int(request.form['NumeroCDAT'])
  SaldoCDAT= int(request.form['SaldoCDAT'])
  SaldoTotalCartera= int(request.form['SaldoTotalCartera'])
  NumeroOperacionesCartera= int(request.form['NumeroOperacionesCartera'])
  NumeroProductosCaptacion= int(request.form['NumeroProductosCaptacion'])
  SaldoTotalCaptaciones= int(request.form['SaldoTotalCaptaciones'])
  NumCreditosVencidos= int(request.form['NumCreditosVencidos'])
  NumeroTCVencidas= int(request.form['NumeroTCVencidas'])
  NumOperacionesCarteraVencida= int(request.form['NumOperacionesCarteraVencida'])
  SaldoTotalCarteraVencida= int(request.form['SaldoTotalCarteraVencida'])
  Regional= int(request.form['Regional'])
  list=[[SexoDesc,Edad,EstadoCivilDesc,ProfesionDesc,indClienteEsEmpleado,TipoClienteDesc,ValorActivos,ValorEgresos,ValorIngresos, 
  ValorOtrosingresos,ValorPatrimonio,TotalPasivos,NumCreditos, SaldoCreditos,
  SaldoCarteraVencida,NumeroTC, SaldoTC, SaldoTCVencido,
  NumeroSobregisrosUso, SaldoSobregirosUso, SaldoSobregirosVencidos,
  NumeroCuentasAhorroActivas, SaldoCuentasAhorroActivas, NumeroCuentasAhorroInactivas, SaldoCuentasAhorroInactivas,
  NumeroCuentasCorrienteActivas,SaldoCuentasCorrienteActivas,
  NumeroCuentascorrienteInactivas,SaldoCuentascorrienteInactivas,
  NumeroCDT,SaldoCDT,NumeroCDAT,SaldoCDAT,SaldoTotalCartera,
  NumeroOperacionesCartera,NumeroProductosCaptacion,
  SaldoTotalCaptaciones,NumCreditosVencidos,NumeroTCVencidas,
  NumOperacionesCarteraVencida, SaldoTotalCarteraVencida, Regional]]
  df2 =pd.DataFrame(list,columns=['SexoDesc', 'Edad', 'EstadoCivilDesc', 'ProfesionDesc',
       'indClienteEsEmpleado', 'TipoClienteDesc', 'ValorActivos',
       'ValorEgresos', 'ValorIngresos', 'ValorOtrosingresos',
       'ValorPatrimonio', 'TotalPasivos', 'NumCreditos', 'SaldoCreditos',
       'SaldoCarteraVencida', 'NumeroTC', 'SaldoTC', 'SaldoTCVencido',
       'NumeroSobregisrosUso', 'SaldoSobregirosUso', 'SaldoSobregirosVencidos',
       'NumeroCuentasAhorroActivas', 'SaldoCuentasAhorroActivas',
       'NumeroCuentasAhorroInactivas', 'SaldoCuentasAhorroInactivas',
       'NumeroCuentasCorrienteActivas', 'SaldoCuentasCorrienteActivas',
       'NumeroCuentascorrienteInactivas', 'SaldoCuentascorrienteInactivas',
       'NumeroCDT', 'SaldoCDT', 'NumeroCDAT', 'SaldoCDAT', 'SaldoTotalCartera',
       'NumeroOperacionesCartera', 'NumeroProductosCaptacion',
       'SaldoTotalCaptaciones', 'NumCreditosVencidos', 'NumeroTCVencidas',
       'NumOperacionesCarteraVencida', 'SaldoTotalCarteraVencida', 'Regional'])
  TD2=joblib.load('model2.pkl')
  y_pred=1-TD2.predict(df2)
  y_pred_probs=TD2.predict_proba(df2)
  y_pred_probs=1-y_pred_probs[:, 1]
  y_pred_probs
  final_results = pd.concat([df2], axis = 1).dropna()
  final_results['predictions'] = y_pred
  final_results["propensity_to_churn(%)"] = y_pred_probs
  final_results["propensity_to_churn(%)"] = final_results["propensity_to_churn(%)"]*100
  final_results["propensity_to_churn(%)"]=final_results["propensity_to_churn(%)"].round(2)

  return render_template('INDIVIDUAL.html', tables=[final_results.to_html(classes='table table-stripped')])
 else:
  return render_template('INDIVIDUAL.html')

@app.route('/DOCUMENTO', methods=['GET', 'POST'])
def get_plot2():
 if request.method == 'POST': 
  df2= pd.read_json(request.form['archivosubido'], lines=True)
  TD2=joblib.load('model2.pkl')
  y_pred=1-TD2.predict(df2)
  y_pred_probs=TD2.predict_proba(df2)
  y_pred_probs=1-y_pred_probs[:, 1]
  y_pred_probs
  final_results = pd.concat([df2], axis = 1).dropna()
  final_results['predictions'] = y_pred
  final_results["propensity_to_churn(%)"] = y_pred_probs
  final_results["propensity_to_churn(%)"] = final_results["propensity_to_churn(%)"]*100
  final_results["propensity_to_churn(%)"]=final_results["propensity_to_churn(%)"].round(2)

  return render_template('DOCUMENTO.html', tables=[final_results.to_html(classes='table table-stripped')])
 else:
  return render_template('DOCUMENTO.html')
  
if __name__ == '__main__':
    app.run(debug=True)