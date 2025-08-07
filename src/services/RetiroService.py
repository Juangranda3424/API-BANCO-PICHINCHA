from src.repository.RetiroRepository import RetiroRepository
from src.repository.DepositoRepository import DepositoRepository

import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class RetiroService:

    def retiro_sin_tarjeta(numeroCuenta,montoRetirar):
        try:
            saldo = RetiroRepository._saldo_actual(numeroCuenta)
            print(f"Saldo actual: {saldo[0]}, Monto a retirar: {montoRetirar}")
            
            # Si el saldo es menor que el monto a retirar, NO se puede realizar el retiro
            if float(saldo[0]) < float(montoRetirar):
                print("Saldo insuficiente para el retiro")
                return False  # Saldo insuficiente
            else:
                print("Saldo suficiente para el retiro")
                return True   # Saldo suficiente
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    @staticmethod
    def retirarMonto_sin_trajeta(codigo):
        try:
            numMax = RetiroRepository._validateNumMaxRetiro(codigo)
            print(numMax[0])
            if int(numMax[0]) == 0:
                return False

            codigoValido = RetiroRepository._retirar_monto(codigo)

            if codigoValido != None:
                resultado = RetiroRepository._getCuenta_monto_max(str(codigoValido[0]))
                if RetiroService._descontarCuenta(resultado[0], resultado[1]):
                    RetiroRepository._updateNumMaxRetiro(numMax[0],codigo)
                    return True
                else:
                    return False
            else:
                return False
                
        except Exception as e:
            print(f"Error: {e}")
            return False
    

    def _descontarCuenta(monto,numeroCuenta):
        saldo = RetiroRepository._saldo_actual(numeroCuenta)
        if float(saldo[0]) < float(monto):
            return False
        else:
            saldo_cuenta_origen = DepositoRepository.saldo_persona(numeroCuenta)
            resultado_origen = float(saldo_cuenta_origen[0]) - float(monto);
            DepositoRepository.actualizacion_saldo_persona(str(resultado_origen),numeroCuenta)
            return True


    @staticmethod
    def _enviar_codigo_acceso(email, nombre_persona):

        try:
            codigo = random.randint(100000, 999999)
    
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            email_usuario = "pichinchabanco254@gmail.com" 
            email_password = "tjrz eisx hzfg imdz"     
            
            mensaje = MIMEMultipart("alternative")
            mensaje['From'] = email_usuario
            mensaje['To'] = email
            mensaje['Subject'] = "🔐 Código de Retiro - Banco Pichincha"
            
            cuerpo_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: 'Arial', sans-serif; margin: 0; padding: 20px; background-color: white; }}
        .container {{ max-width: 600px; margin: 0 auto; background-color: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 2px solid black; }}
        .header {{ background-color: #FFD700; color: black; padding: 30px; text-align: center; border-bottom: 2px solid black; }}
        .logo {{ font-size: 28px; font-weight: bold; margin-bottom: 10px; color: black; }}
        .slogan {{ font-size: 14px; color: black; }}
        .content {{ padding: 40px 30px; background-color: white; }}
        .greeting {{ font-size: 18px; color: black; margin-bottom: 20px; }}
        .code-section {{ text-align: center; margin: 30px 0; }}
        .code-label {{ font-size: 16px; color: black; margin-bottom: 15px; }}
        .code-box {{ display: inline-block; background-color: #FFD700; color: black; font-size: 32px; font-weight: bold; padding: 20px 40px; border-radius: 10px; letter-spacing: 3px; border: 3px solid black; }}
        .instructions {{ background-color: #FFFACD; border-left: 4px solid #FFD700; padding: 20px; margin: 30px 0; border-radius: 5px; border: 1px solid black; }}
        .instructions h3 {{ color: black; margin-top: 0; font-size: 16px; }}
        .instructions ul {{ color: black; margin: 10px 0; padding-left: 20px; }}
        .instructions li {{ margin: 8px 0; }}
        .locations {{ background-color: white; padding: 20px; border-radius: 8px; margin: 20px 0; border: 2px solid #FFD700; }}
        .locations h3 {{ color: black; margin-top: 0; }}
        .locations ul {{ color: black; }}
        .contact {{ background-color: #FFFACD; padding: 20px; border-radius: 8px; margin: 20px 0; border: 1px solid black; }}
        .contact h3 {{ color: black; margin-top: 0; }}
        .contact-info {{ color: black; }}
        .footer {{ background-color: black; color: white; padding: 30px; text-align: center; font-size: 12px; }}
        .footer-info {{ margin: 5px 0; }}
        .warning {{ color: black; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">🏦 BANCO PICHINCHA</div>
            <div class="slogan">"Contigo en cada paso"</div>
        </div>
        
        <div class="content">
            <div class="greeting">Estimado/a {nombre_persona},</div>
            
            <div class="code-section">
                <div class="code-label">🔐 Su código de retiro sin tarjeta es:</div>
                <div class="code-box">{codigo}</div>
            </div>
            
            <div class="instructions">
                <h3>⚠️ INSTRUCCIONES IMPORTANTES</h3>
                <ul>
                    <li><strong>Tiempo válido:</strong> Este código expira en <span class="warning">5 minutos</span></li>
                    <li><strong>Uso:</strong> Úselo en cualquier cajero automático Pichincha</li>
                    <li><strong>Seguridad:</strong> NO comparta este código con terceros</li>
                    <li><strong>Importante:</strong> Si no solicitó este retiro, ignore este mensaje</li>
                </ul>
            </div>
            
            <div class="locations">
                <h3>📍 Encuentre nuestros cajeros en:</h3>
                <ul>
                    <li>🏢 Sucursales Banco Pichincha</li>
                    <li>🛒 Centros comerciales principales</li>
                    <li>🏪 Red extendida de cajeros automáticos</li>
                    <li>⛽ Estaciones de servicio</li>
                </ul>
            </div>
            
            <div class="contact">
                <h3>💬 ¿Necesita ayuda?</h3>
                <div class="contact-info">
                    📞 <strong>Línea de atención:</strong> *222<br>
                    📧 <strong>Email:</strong> atencion@pichincha.com<br>
                    🌐 <strong>Web:</strong> www.pichincha.com<br>
                    📱 <strong>App móvil:</strong> Pichincha Mi Banco
                </div>
            </div>
        </div>
        
        <div class="footer">
            <div class="footer-info">Este mensaje es generado automáticamente. No responda a este correo.</div>
            <div class="footer-info">───────────────────────────────────────────────────────────</div>
            <div class="footer-info"><strong>Banco Pichincha S.A.</strong> | RUC: 1790010937001</div>
            <div class="footer-info">Av. Amazonas y Pereira | Quito - Ecuador</div>
            <div class="footer-info">© 2025 Banco Pichincha. Todos los derechos reservados.</div>
        </div>
    </div>
</body>
</html>
            """
            
            cuerpo_texto = f"""
BANCO PICHINCHA - Código de Retiro

Estimado/a {nombre_persona},

Su código de retiro sin tarjeta es: {codigo}

IMPORTANTE: Este código es válido por 5 minutos únicamente.

Banco Pichincha
            """
            
            # Adjuntar ambas versiones
            parte_texto = MIMEText(cuerpo_texto, 'plain', 'utf-8')
            parte_html = MIMEText(cuerpo_html, 'html', 'utf-8')
            
            mensaje.attach(parte_texto)
            mensaje.attach(parte_html)
            
            # Enviar email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_usuario, email_password)
            text = mensaje.as_string()
            server.sendmail(email_usuario, email, text)
            server.quit()
            
            print(f"📧 Email enviado a {email}")
            return codigo
        except Exception as e:
            print(f"Error enviando email: {e}")
            return None