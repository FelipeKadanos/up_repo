Console.WriteLine("Felipe Kadanos - 2026 - Address Api");

// Microsoft.EntityFrameworkCore.Sqlite
// Dentro do projeto:
// dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 8.0.31
// dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 7.0.0
// dotnet add package Microsoft.EntityFrameworkCore.Design --version 8.0.31
// dotnet add package Microsoft.EntityFrameworkCore.Design --version 7.0.0

using Microsoft.AspNetCore.Mvc;

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
app.MapPost("/api/produto/cadastrar", ([FromBody] Produto? produto) => { // O ? diz que o produto pode ser nulo
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
app.MapGet("/api/produto/buscar/{nome}", ([FromRoute] string nome) => {
    Produto? produto = pdts.FirstOrDefault(p => p.Nome == nome);
    
    /* foreach (Produto pdt in pdts) {
        if (pdt.Nome == nome)
            return Results.Ok(pdt);
    } */
    
    return (produto is null) ? Results.NotFound("Produto não encontrado") : Results.Ok(produto);
});

// DEL: http://localhost/api/produto/excluir/{nome}
app.MapDel("/api/produto/excluir/{id}", ([FromRoute] string id) => {
    Produto? produto = pdts.FirstOrDefault(p => p.Id == id);

    if (produto is null)
        return Results.NotFound("Produto não encontrado");

    pdts.Remove(produto)
    return Results.Ok(produto);
});

// PUT: http://localhost/api/produto/alterar/{nome}
app.MapPut("/api/produto/alterar/{id}", ([FromRoute] string id, [FromBody] Produto produto) => {
    Produto? produto = pdts.FirstOrDefault(p => p.Id == id);
    
    if (produto is null)
        return Results.NotFound("Produto não encontrado");

    
    return Results.Ok(produto);
});

app.Run();