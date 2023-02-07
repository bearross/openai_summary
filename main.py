import openai
openai.api_key = "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"
model_engine = "text-davinci-003"
prefix_oneshot = """Here are a list of Press Releases and their Summary and Key Takeaways.
####
Press Release: 
Third approved indication for SKYRIZI (risankizumab-rzaa) is supported by safety and efficacy data from two induction and one maintenance clinical trials evaluating SKYRIZI in moderately to severely active Crohn's disease, ADVANCE, MOTIVATE and FORTIFY1-4
- As early as week 4 in the induction studies, clinical response and clinical remission were achieved by significantly more subjects treated with SKYRIZI versus placebo, as were co-primary endpoints of endoscopic response and clinical remission at week 12 and week 521-4
- Crohn's disease is chronic, systemic and progressive; most patients experience unpredictable symptoms that have a significant impact on daily life5-8
NORTH CHICAGO, Ill., June 17, 2022 /PRNewswire/ -- AbbVie (NYSE: ABBV) today announced that the U.S. Food and Drug Administration (FDA) has approved SKYRIZI® (risankizumab-rzaa) as the first and only specific interleukin-23 (IL-23) inhibitor for the treatment of adults with moderately to severely active Crohn's disease (CD).4 In two induction and one maintenance clinical trials, SKYRIZI demonstrated significant improvements in endoscopic response (defined as a decrease of greater than 50% from the baseline Simple Endoscopic Score in CD [SES-CD] or for patients with isolated ileal disease and SES-CD of 4, at least a 2-point reduction from baseline) and clinical remission (defined as a Crohn's Disease Activity Index [CDAI] of less than 150), compared to placebo, as both an induction and maintenance therapy.4
Experience the interactive Multimedia News Release here: https://www.multivu.com/players/English/8978352-abbvie-fda-crohns-disease/ 
"We are proud to offer the first new treatment option in six years for moderately to severely active CD, which may provide patients with a meaningful level of endoscopic improvement," said Thomas Hudson, M.D., senior vice president, research and development, chief scientific officer, AbbVie. "With more than 30 ongoing or planned trials in inflammatory bowel disease, AbbVie is committed to advancing the standards of care for patients by exploring and investing in research for those living with immune-mediated, gastroenterological conditions."
The dosing regimen for SKYRIZI for the treatment of CD is 600 mg administered by intravenous infusion over at least one hour at week 0, week 4, and week 8, followed by 360 mg self-administered by subcutaneous injection (SC) with an on-body injector (OBI) at week 12, and every 8 weeks thereafter.4 A 180 mg self-administered SC maintenance dose option remains under review by the FDA.
Endoscopic and Clinical Outcomes1-4 
The co-primary endpoints of the clinical trials were endoscopic response and clinical remission. In the 12-week induction studies, ADVANCE and MOTIVATE, a significantly greater proportion of patients treated with SKYRIZI achieved endoscopic response and clinical remission compared to placebo. As early as week 4, clinical response (defined as a 100-point reduction in CDAI) and clinical remission were achieved in a significantly greater proportion of patients receiving SKYRIZI as compared to placebo.
In the 52-week maintenance trial, FORTIFY, a significantly greater proportion of patients achieved the co-primary endpoints of endoscopic response and clinical remission as compared with the placebo group (risankizumab induction responders) after one year.
"In both the induction and maintenance clinical trials, a significantly greater number of adult patients saw few or no symptoms and a meaningful reduction of visible signs of intestinal inflammation, compared to placebo," said Marla Dubinsky, M.D., chief, division of pediatric gastroenterology for the Mount Sinai Health System, co-director of the Susan and Leonard Feinstein IBD Center at Mount Sinai.* "This approval provides healthcare professionals with a greatly needed additional option for treating the disruptive symptoms of Crohn's disease." 
Summary:
AbbVie announced approval of Skyrizi in CD (3 IV induction doses of 600 mg; 360mg SC maintenance dosing with OBI Q8W)
Key Takeaways: 
● On June 17, AbbVie announced FDA approval of Skyrizi for the treatment of adults with moderate to severe Crohn's Disease
● Dosing regimen: 3 IV induction doses of 600mg Q4W, followed by 360mg SC maintenance dose with an On-body injector (OBI) at W12 and Q8W thereafter
● FDA review of 180 mg self-administered SC maintenance dose option ongoing
● Approval is supported by Phase 3 pivotal studies – ADVANCE, MOTIVATE, and FORTIFY. FORTIFY study includes a sub-study evaluating an OBI
####
"""
INPUT_PRESS_RELEASE = """
KemPharm Partners with the Hypersomnia Foundation to Support Sleep Disorder Research and Advocacy January 18, 2023 at 7:30 AM EST KemPharm advancing multicenter Phase 2 clinical trial investigating the efficacy and safety of KP1077 for the treatment of idiopathic hypersomnia (IH) CELEBRATION, Fla., Jan. 18, 2023 (GLOBE NEWSWIRE) -- KemPharm, Inc. (NasdaqGS: KMPH) (KemPharm, or the Company), a rare disease therapeutics company focused on the development of treatments for rare central nervous system (CNS) disorders, neurodegenerative diseases, lysosomal storage disorders and related treatment areas, announced its partnership with the Hypersomnia Foundation, which engages, informs and champions the global community to improve the lives of people with idiopathic hypersomnia (IH) and related sleep disorders. IH is a chronic neurologic disorder marked by significant detrimental effects on nighttime sleep as well as daytime sleepiness/wakefulness. It is estimated that approximately 37,000 patients are currently diagnosed with IH and seeking treatment, although the total population may be much larger due to patients not seeking treatment or having not been diagnosed. KemPharm is currently investigating KP1077 in a double-blind, placebo-controlled, randomized-withdrawal, dose-optimizing, multi-center Phase 2 clinical trial evaluating the efficacy and safety of KP1077 for the treatment of IH. KemPharm expects to enroll approximately 48 adult patients with IH in more than 30 centers in the United States. Additional details about the study, how to enroll, and available study sites can be found on www.clinicaltrials.gov (NCT05668754). “We are pleased to be working in coordination with the Hypersomnia Foundation to increase awareness and knowledge of idiopathic hypersomnia for patients, caregivers and clinicians to better understand the condition and advance research, with the ultimate goal of faster diagnosis and improved outcomes,” said Richard W. Pascoe, Chief Executive Officer of KemPharm. “IH is a rare sleep disorder for which few treatment options exist. We believe KP1077 has the potential to address the most debilitating symptoms of IH, and we look forward to advancing the recently initiated Phase 2 clinical trial of KP1077 in IH with support from patient groups, including the Hypersomnia Foundation.” “We are deeply grateful for the work KemPharm is doing to advance treatments for our community at such a time when pharmacological options for people with IH are so desperately lacking,” said Claire Crisp, MFA, Chief Executive officer of the Hypersomnia Foundation. “Support from sponsors like KemPharm are key to our efforts to advocate for and support those dealing with debilitating sleep disorders.”
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


