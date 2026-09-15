public class Produto {
    
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Nome { get; set; } = string.Empty;
    public DateTime Cadastro { get; set; } = DateTime.Now;
}
