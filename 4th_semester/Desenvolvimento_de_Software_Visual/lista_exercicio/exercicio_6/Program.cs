Console.Clear();
// Exercicio 6a
// 1- Criar um vetor numerico
// 2- Necessario um laço de repetição
// 3- Gerar os valores aleatorios
// 4- Guardar os valores  dentro de um vetor

// Criar um vetor de valores numéricos
int[] nums = new int[100];

Random random = new Random();

// Necessário um laço de repetição - FOR
for (int i = 0; i < nums.Length; i++) {
    nums[i] = random.Next(1000); // Gera valores aleatorios e os guarda
}

Console.WriteLine("--- VETOR ORIGINAL ---");
printArray(nums);

// 5 - Percorrer o vetor com um laço repetição
// 6 - Compara se a posição atual é maior que a proxima
// 7 - Se for maior, realizar a troca de valores
// 8 - Verificar se o maior valor está na ultima posição 
for (int i = 0; i < nums.Length; i++) {
    for (int j = 0; j < nums.Length - 1; j++) {
        if (nums[j] > nums[j + 1]) {
            int aux = nums[j];
            nums[j] = nums[j + 1];
            nums[j + 1] = aux;
        }
    }
}

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