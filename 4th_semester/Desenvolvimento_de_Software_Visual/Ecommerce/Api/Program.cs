try
{
    if (!Console.IsOutputRedirected)
    {
        Console.Clear();
    }
}
catch (IOException)
{
    // Some hosts do not expose a clearable console.
}
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

app.MapGet("/api/produto/listar", () => {
    return produtos;
});

app.MapPost("/api/produto/cadastrar", (Produto produto) => {
    produtos.Add(produto);
    // return Results.Created($"/api/produto/{produto.Id}", produto);
    return Results.Created("", produto);
});

/* Exercicio:
 * 1- Pesquisar produto por nome
 * 2- Remover um produto
 * 3- Alterar um produto
 */

app.Run();