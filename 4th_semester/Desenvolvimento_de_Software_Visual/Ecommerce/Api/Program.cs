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

List<Produto> pdts = new() {
    new Produto { Nome = "Notebook" },
};

app.MapGet("/", () => "Bem-vindo à API de Endereços!");

// GET: http://localhost/api/produto/listar
app.MapGet("/api/produto/listar", () => {
    return pdts;
});

// POST: http://localhost/api/produto/cadastrar
app.MapPost("/api/produto/cadastrar", (Produto? produto) => { // O ? diz que o produto pode ser nulo

    if (produto is null)
        return Results.BadRequest("Produto não foi enviado.");
    
    foreach (var pdt in pdts) {
        if (pdt.Nome == produto.Nome)
            return Results.BadRequest("Produto já cadastrado.");
    }
    
    pdts.Add(produto);
    return Results.Created("", produto);
    // return Results.Created($"/api/produto/{produto.Id}", produto);
});

// GET: http://localhost/api/produto/buscar/{nome}
app.MapGet("/api/produto/buscar/{nome}", (string nome) => {
    
    foreach (Produto pdt in pdts) {
        if (pdt.Nome == nome)
            return Results.Ok(pdt);
    }
    
    return Results.NotFound("Produto não encontrado");
});

/* Exercicio:
 * 2- Remover um produto
 * 3- Alterar um produto
 */

app.Run();