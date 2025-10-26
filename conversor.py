import customtkinter as ctk
import conversor_temperatura as temp
import conversor_distancia as dist
import conversor_peso as peso

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Conversor de Unidades")
app.geometry("600x450")
app.resizable(False, False)

def criar_interface(aba, tipo, opcoes):
    frame = ctk.CTkFrame(aba)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    frame.grid_columnconfigure(0, weight=1)

    # Ajuste do título
    titulo_texto = ""
    if tipo == "temp":
        titulo_texto = "Temperatura"
    elif tipo == "dist":
        titulo_texto = "Distância"
    elif tipo == "peso":
        titulo_texto = "Peso"

    label_titulo = ctk.CTkLabel(frame, text=f"Conversor de {titulo_texto}", font=("Arial", 20, "bold"))
    label_titulo.grid(row=0, column=0, pady=(10, 20), sticky="n")

    entrada_valor = ctk.CTkEntry(frame, width=200, placeholder_text="Digite o valor")
    entrada_valor.grid(row=1, column=0, pady=10, sticky="n")

    combo_origem = ctk.CTkOptionMenu(frame, values=opcoes)
    combo_origem.grid(row=2, column=0, pady=8, sticky="n")
    combo_origem.set(opcoes[0])

    combo_destino = ctk.CTkOptionMenu(frame, values=opcoes)
    combo_destino.grid(row=3, column=0, pady=8, sticky="n")
    combo_destino.set(opcoes[1] if len(opcoes) > 1 else opcoes[0])

    label_resultado = ctk.CTkLabel(frame, text="", font=("Arial", 16, "bold"))
    label_resultado.grid(row=5, column=0, pady=(15, 5), sticky="n")

    def on_converter():
        valor_str = entrada_valor.get().strip().replace(",", ".")
        if not valor_str:
            label_resultado.configure(text="Insira um valor.")
            return
        try:
            valor = float(valor_str)
        except ValueError:
            label_resultado.configure(text="Valor inválido.")
            return

        origem = combo_origem.get()
        destino = combo_destino.get()
        resultado = None

        if tipo == "temp":
            if origem == "Celsius" and destino == "Fahrenheit":
                resultado = temp.celsius_para_fahrenheit(valor)
            elif origem == "Fahrenheit" and destino == "Celsius":
                resultado = temp.fahrenheit_para_celsius(valor)
            elif origem == "Celsius" and destino == "Kelvin":
                resultado = temp.celsius_para_kelvin(valor)
            elif origem == "Kelvin" and destino == "Celsius":
                resultado = temp.kelvin_para_celsius(valor)
            elif origem == "Fahrenheit" and destino == "Kelvin":
                resultado = temp.fahrenheit_para_kelvin(valor)
            elif origem == "Kelvin" and destino == "Fahrenheit":
                resultado = temp.kelvin_para_fahrenheit(valor)
            elif origem == destino:
                resultado = valor

        elif tipo == "dist":
            if origem == "Km" and destino == "Milhas":
                resultado = dist.km_para_milhas(valor)
            elif origem == "Milhas" and destino == "Km":
                resultado = dist.milhas_para_km(valor)
            elif origem == "Metros" and destino == "Km":
                resultado = dist.metros_para_km(valor)
            elif origem == "Km" and destino == "Metros":
                resultado = dist.km_para_metros(valor)
            elif origem == "Metros" and destino == "Milhas":
                resultado = dist.metros_para_milhas(valor)
            elif origem == "Milhas" and destino == "Metros":
                resultado = dist.milhas_para_metros(valor)
            elif origem == destino:
                resultado = valor

        elif tipo == "peso":
            if origem == "Kg" and destino == "Libras":
                resultado = peso.kg_para_lb(valor)
            elif origem == "Libras" and destino == "Kg":
                resultado = peso.lb_para_kg(valor)
            elif origem == "Kg" and destino == "Gramas":
                resultado = peso.kg_para_g(valor)
            elif origem == "Gramas" and destino == "Kg":
                resultado = peso.g_para_kg(valor)
            elif origem == "Gramas" and destino == "Libras":
                resultado = peso.g_para_lb(valor)
            elif origem == "Libras" and destino == "Gramas":
                resultado = peso.lb_para_g(valor)
            elif origem == destino:
                resultado = valor

        if resultado is not None:
            if resultado == int(resultado):
                resultado_formatado = f"{int(resultado)}"
            else:
                resultado_formatado = f"{resultado:.2f}"
            label_resultado.configure(
                text=f"{valor} {origem} → {resultado_formatado} {destino}"
            )
        else:
            label_resultado.configure(text="Conversão não suportada.")

    botao_converter = ctk.CTkButton(frame, text="Converter", width=160, command=on_converter)
    botao_converter.grid(row=4, column=0, pady=(10,5), sticky="n")


    botao_limpar = ctk.CTkButton(frame, text="Limpar", width=100,
                                 command=lambda: [entrada_valor.delete(0, "end"),
                                                  combo_origem.set(opcoes[0]),
                                                  combo_destino.set(opcoes[1] if len(opcoes) > 1 else opcoes[0]),
                                                  label_resultado.configure(text="")])
    botao_limpar.grid(row=6, column=0, pady=(5,10), sticky="n")


abas = ctk.CTkTabview(app, width=560, height=380)
abas.pack(pady=20)

aba_temp = abas.add("Temperatura")
aba_dist = abas.add("Distância")
aba_peso = abas.add("Peso")

criar_interface(aba_temp, "temp", ["Celsius", "Fahrenheit", "Kelvin"])
criar_interface(aba_dist, "dist", ["Km", "Milhas", "Metros"])
criar_interface(aba_peso, "peso", ["Kg", "Libras", "Gramas"])

app.mainloop()
