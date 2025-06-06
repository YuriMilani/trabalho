def loginUsuario(perfil):
    perfil_lower = perfil.lower()
    if perfil_lower == 'admin':
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")

# Test
loginUsuario("Admin")
loginUsuario("admin")
loginUsuario("User")
loginUsuario("usuário")
loginUsuario("etc")