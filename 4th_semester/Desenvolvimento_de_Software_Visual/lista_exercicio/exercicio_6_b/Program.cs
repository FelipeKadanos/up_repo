Console.Clear();
// Exercicio 6b

// Mesmo exercicio do 6a porem utilizando um metodo de ordenação do C#

// Criar um vetor de valores numéricos      
int[] nums = new int[100];

Random random = new Random();

// Necessário um laço de repetição - FOR
for (int i = 0; i < nums.Length; i++) {
    nums[i] = random.Next(1000); // Gera valores aleatorios e os guarda
}

Console.WriteLine("--- VETOR ORIGINAL ---");
printArray(nums);

Array   .Sort(nums);

Console.WriteLine("\n--- VETOR APÓS UMA PASSAGEM ---");
printArray(nums);

void printArray(int[] nums) {
    for (int i = 0; i < nums.Length; i++) {
        string indice = (i + 1).ToString().PadLeft(3); // Garante 3 caracteres para o índice
        string valor = nums[i].ToString().PadLeft(3);   // Garante 3 caracteres para o número aleatório
        string quebraLinha = ((i + 1) % 10 == 0) ? "\n" : "";

        Console.Write($"{indice} - {valor}; {quebraLinha}");
    }
}