import openai
openai.api_key = "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"
model_engine = "text-davinci-003"
prefix_oneshot = """Here are a list of Press Releases and their Summary and Key Takeaways.
####
Press Release: 

Summary:

Key Takeaways: 
●
●
●
●
####
"""
INPUT_PRESS_RELEASE = """
Approval marks fourth indication for VRAYLAR, backed by proven efficacy and well-established tolerability as an adjunctive treatment for major depressive disorder (MDD) with an antidepressant therapy (ADT), showing improvement in symptoms when compared to placebo + ADT Designed for specific mood disorders, VRAYLAR is now the first and only dopamine and serotonin partial agonist FDA-approved for the most common forms of depression – as an adjunctive treatment for MDD and the treatment of depressive episodes associated with bipolar I disorder
About one in five U.S. adults will experience MDD during their lifetime, and many of them may have partial response to the treatment with an ADT
NORTH CHICAGO, Ill., Dec. 16, 2022 /PRNewswire/ -- AbbVie (NYSE: ABBV) today announced that the U.S. Food and Drug Administration (FDA) has approved VRAYLAR®(cariprazine) as an adjunctive therapy to antidepressants for the treatment of major depressive disorder (MDD) in adults. Supported by clinical data demonstrating efficacy and well-established tolerability, this additional indication provides a new option for adults who have a partial response to the treatment of an antidepressant.
Experience the interactive Multimedia News Release here: https://www.multivu.com/players/English/9107351-vraylar-cariprazine-fda-approval-major-depressive-disorder/
"Many living with major depressive disorder find that their ongoing antidepressant therapy doesn't offer meaningful relief from the symptoms they experience every day," said Thomas Hudson, M.D., senior vice president, research and development, chief scientific officer, AbbVie. "Today's approval of VRAYLAR provides an important new treatment option to meet a critical unmet medical need. AbbVie is committed to driving progress and advancing solutions for patients living with complex neuropsychiatric conditions."
MDD is one of the most common mental disorders in the U.S.; approximately one in five adults will experience this disorder during their lifetime.In a large U.S. study of adults with MDD, approximately 50 percent still had depressive symptoms with their first antidepressant.If some symptoms of depression persist while on an antidepressant, adding a different type of medication, often referred to as an adjunctive treatment, to the existing regimen may help.
"Patients with inadequate response to standard antidepressant medication are often frustrated by the experience of trying multiple medicines and still suffering from unresolved symptoms. Instead of starting over with another standard antidepressant, VRAYLAR works with an existing treatment and can help build on the progress already made," said Gary Sachs, MD, clinical vice president at Signant Health, associate clinical professor of psychiatry at Massachusetts General Hospital, and lead Phase 3 clinical trial investigator. "For adults living with major depressive disorder, because of inadequate improvement in response to standard antidepressants, VRAYLAR is an efficacious adjunctive treatment option with a well-characterized safety profile."
Cariprazine is marketed as VRAYLAR®in the U.S., and in addition to being approved as an adjunctive therapy to antidepressants for the treatment of MDD in adults, it is FDA-approved to treat adults with depressive, acute manic and mixed episodes associated with bipolar I disorder, as well as schizophrenia. Cariprazine is co-developed by AbbVie and Gedeon Richter Plc. More than 8,000 patients worldwide have been treated with cariprazine across more than 20 clinical trials evaluating the efficacy and safety of cariprazine for a broad range of psychiatric disorders.
"When we were in the early stages of development for cariprazine, we focused on designing a compound that covers a range of symptoms for mental health conditions and affects the dopamine D3 receptor," said István Greiner, Ph.D., research and development, director, Gedeon Richter. "While schizophrenia and bipolar manic and mixed episodes were the first indications in the U.S. market, we are thrilled to see the full potential of cariprazine unlocked with approvals in bipolar I depression, and now, as an antidepressant adjunct in major depressive disorder."
Highlights from the clinical program supporting the approval include:
A Phase 3 Study 3111-301-001 showed a clinically and statistically significant change from baseline to week six in the Montgomery-Åsberg Depression Rating Scale (MADRS) total score for patients treated with cariprazine at 1.5 mg/day + ADT compared with placebo + ADT. A second registration-enabling study, RGH-MD-75, showed a clinically and statistically significant change from baseline to week eight in the MADRS total score for patients treated with cariprazine at 2-4.5 mg/day (mean dose 2.6 mg) + ADT compared with placebo + ADT.
Cariprazine was generally well tolerated in 6- and 8-week studies. Mean weight change was < 2lbs and ≤ 3% of patients had a weight increase of ≥ 7%.
The starting dosage of VRAYLAR is 1.5 mg once daily. Depending upon clinical response and tolerability, the dosage can be increased to 3 mg once daily on Day 15. In clinical trials, dosage titration at intervals of less than 14 days resulted in a higher incidence of adverse reactions. The maximum recommended dosage is 3 mg once daily.
Most common adverse reactions observed in the adjunctive MDD studies (≥ 5% and at least twice the rate of placebo) were:
Akathisia, nausea, and insomnia at the recommended doses in 6-week, fixed-dose trials
Akathisia, restlessness, fatigue, constipation, nausea, increased appetite, dizziness, insomnia, and extrapyramidal symptoms in one 8-week flexible-dose trial at a titration of less than 14 days.
"""
prompt=prefix_oneshot+"\nPress Release:\n"+INPUT_PRESS_RELEASE+"Summary:\n"
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.6,
)

response = completion.choices[0].text
print("Summary: ", response)


