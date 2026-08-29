print("🔍 VERIFICADOR DE URL 🔍")

url = input("\nDigite a URL de um site: ")

if url.startswith("https://"):

    print("🔐 Este site usa HTTPS (seguro)")

elif url.startswith("http://"):

    print("👀 Este site usa HTTP (não seguro)")

else:

    print("❌ Isso não parece ser uma URL completa")