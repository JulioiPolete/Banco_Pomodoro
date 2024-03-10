import tkinter as tk
from tkinter import messagebox

def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    dinheiro_conta = 5440

    if usuario == 'Marcos' and senha == '1254':
        messagebox.showinfo("Bem-vindo", f"Seja bem-vindo, {usuario}, ao seu Banco Pomodoro!\nSeu saldo é de R${dinheiro_conta}")
        opcao = opcao_var.get()
        if opcao == 'Saque':
            realizar_saque(dinheiro_conta)
        elif opcao == 'Transferência':
            realizar_transferencia(dinheiro_conta)
        elif opcao == 'Depósito':
            realizar_deposito(dinheiro_conta)
        else:
            messagebox.showerror("Erro", "Opção inválida")
    else:
        messagebox.showerror("Erro", "Credenciais inválidas")

def realizar_saque(saldo):
    saque_window = tk.Toplevel(janela)
    saque_window.title("Saque")

    tk.Label(saque_window, text="Qual o valor que deseja sacar:").pack()
    entrada_saque = tk.Entry(saque_window)
    entrada_saque.pack()

    def processar_saque():
        try:
            valor_saque = float(entrada_saque.get())
            if valor_saque > saldo:
                messagebox.showerror("Erro", "Saldo insuficiente!")
            else:
                novo_saldo = saldo - valor_saque
                messagebox.showinfo("Saque", f"O valor sacado foi de R${valor_saque}, seu saldo atual agora é de R${novo_saldo}")
                saque_window.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o saque.")

    botao_confirmar_saque = tk.Button(saque_window, text="Confirmar", command=processar_saque)
    botao_confirmar_saque.pack()

def realizar_transferencia(saldo):
    transferencia_window = tk.Toplevel(janela)
    transferencia_window.title("Transferência")

    tk.Label(transferencia_window, text="Qual o valor que deseja transferir:").pack()
    entrada_transferencia = tk.Entry(transferencia_window)
    entrada_transferencia.pack()

    def processar_transferencia():
        try:
            valor_transferencia = float(entrada_transferencia.get())
            if valor_transferencia > saldo:
                messagebox.showerror("Erro", "Saldo insuficiente!")
            else:
                novo_saldo = saldo - valor_transferencia
                messagebox.showinfo("Transferência", f"O valor transferido foi de R${valor_transferencia}, seu saldo atual agora é de R${novo_saldo}")
                transferencia_window.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para a transferência.")

    botao_confirmar_transferencia = tk.Button(transferencia_window, text="Confirmar", command=processar_transferencia)
    botao_confirmar_transferencia.pack()

def realizar_deposito(saldo):
    deposito_window = tk.Toplevel(janela)
    deposito_window.title("Depósito")

    tk.Label(deposito_window, text="Qual o valor que deseja depositar:").pack()
    entrada_deposito = tk.Entry(deposito_window)
    entrada_deposito.pack()

    def processar_deposito():
        try:
            valor_deposito = float(entrada_deposito.get())
            novo_saldo = saldo + valor_deposito
            messagebox.showinfo("Depósito", f"O valor depositado foi de R${valor_deposito}, seu saldo atual agora é de R${novo_saldo}")
            deposito_window.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o depósito.")

    botao_confirmar_deposito = tk.Button(deposito_window, text="Confirmar", command=processar_deposito)
    botao_confirmar_deposito.pack()

# Criar janela principal
janela = tk.Tk()
janela.title("Banco Pomodoro")

# Criar widgets
tk.Label(janela, text="Usuário:").grid(row=0, column=0, padx=10, pady=5)
entrada_usuario = tk.Entry(janela)
entrada_usuario.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=5)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.grid(row=1, column=1, padx=10, pady=5)

opcao_var = tk.StringVar(janela)
opcao_var.set("Saque")  # Opção padrão
opcoes = ["Saque", "Transferência", "Depósito"]
opcao_menu = tk.OptionMenu(janela, opcao_var, *opcoes)
opcao_menu.grid(row=2, column=1, padx=10, pady=5)

botao_login = tk.Button(janela, text="Login", command=fazer_login)
botao_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Rodar a interface
janela.mainloop()
