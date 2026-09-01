Console.Clear();
Console.WriteLine("Felipe Kadanos - 2026 - Address Api");

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

List<Produto> produtos = new() {
    new Produto { Nome = "Notebook" },
    new Produto { Nome = "Smartphone" },
    new Produto { Nome = "Monitor" },
    new Produto { Nome = "Teclado" },
    new Produto { Nome = "Mouse" },
    new Produto { Nome = "Headset" },
    new Produto { Nome = "Webcam" },
    new Produto { Nome = "Impressora" },
    new Produto { Nome = "Roteador" },
    new Produto { Nome = "Caixa de Som" }
};

app.MapGet("/", () => "Bem-vindo à API de Endereços!");
app.MapGet("/api/produto", () => {
    return produtos;
});

Produto produto = new Produto();
produto.Nome = "Teclado";
Console.WriteLine($"Produto: {produto.Nome}");

app.Run();
