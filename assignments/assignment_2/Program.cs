using System;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

string codeContent = File.ReadAllText("BadCodeExample.cs");

string apiKey = "your-openai-api-key"; // Replace with your OpenAI API Key
string apiURL = "https://api.groq.com/openai/v1/chat/completions";

using HttpClient client = new HttpClient();
client.DefaultRequestHeaders.Add("Authorization", $"Bearer {apiKey}");

var requestData = new
{
    model = "llama3-70b-8192",
    messages = new [] {
        new {
            role = "system",
            content = "### Instruction ###\nYou are a code QA tester. You are looking at provided code and give a comprehensive report on the code quality."
        },
        new {
            role = "user",
            content = "### Code ###\n" + codeContent
        }
    },
    max_tokens = 500,
    temperature = 0.5
};

string json = Newtonsoft.Json.JsonConvert.SerializeObject(requestData);
StringContent content = new StringContent(json, Encoding.UTF8, "application/json");

HttpResponseMessage response = await client.PostAsync(apiURL, content);
if (!response.IsSuccessStatusCode)
    throw new Exception($"Failed to analyze code: {response.StatusCode}");

var responseContent = await response.Content.ReadAsStringAsync();
dynamic result = Newtonsoft.Json.JsonConvert.DeserializeObject(responseContent);

string report = result.choices[0].message.content;
Console.WriteLine("Analysis Report:");
Console.WriteLine(report);

return;