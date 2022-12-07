# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Test Analysis

### Problem Statement
This project analyzes SAT results for students applying to different majors or colleges. The aim is to provide recommendations for students, especially those who may not have a clear preference on major or college. Hence, the insights are meant to facilitate decision-making processs for students in deciding what majors or colleges to go for.

---
### Contents:
- [Background](#Background)
- [Data Import & Cleaning](#Data-Import-and-Cleaning)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Data Visualization](#Visualize-the-Data)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)

---
### Background

The SAT and ACT are standardized tests that many colleges and universities in the United States require for their admissions process. This score is used along with other materials such as grade point average (GPA) and essay responses to determine whether or not a potential student will be accepted to the university.

The SAT has two sections of the test: Evidence-Based Reading and Writing and Math ([*source*](https://www.princetonreview.com/college/sat-sections)). The ACT has 4 sections: English, Mathematics, Reading, and Science, with an additional optional writing section ([*source*](https://www.act.org/content/act/en/products-and-services/the-act/scores/understanding-your-scores.html)). They have different score ranges, which you can read more about on their websites or additional outside sources (a quick Google search will help you understand the scores for each test):
* [SAT](https://collegereadiness.collegeboard.org/sat)
* [ACT](https://www.act.org/content/act/en.html)

Standardized tests have long been a controversial topic for students, administrators, and legislators. Since the 1940's, an increasing number of colleges have been using scores from sudents' performances on tests like the SAT and the ACT as a measure for college readiness and aptitude ([*source*](https://www.minotdailynews.com/news/local-news/2017/04/a-brief-history-of-the-sat-and-act/)). Supporters of these tests argue that these scores can be used as an objective measure to determine college admittance. Opponents of these tests claim that these tests are not accurate measures of students potential or ability and serve as an inequitable barrier to entry. Lately, more and more schools are opting to drop the SAT/ACT requirement for their Fall 2021 applications ([*read more about this here*](https://www.cnn.com/2020/04/14/us/coronavirus-colleges-sat-act-test-trnd/index.html)).

### Datasets
The datasets used in the analysis were as follows:

* [`sat_2019_by_intended_college_major.csv`](./data/sat_2019_by_intended_college_major.csv): 2019 SAT Scores by Intended College Major ([source](https://reports.collegeboard.org/media/pdf/2019-total-group-sat-suite-assessments-annual-report.pdf))
* [`sat_act_by_college.csv`](./data/sat_act_by_college.csv): Ranges of Accepted ACT & SAT Student Scores by Colleges ([source](https://www.compassprep.com/college-profiles/))

---

### Outside Research

The total SAT score is a number between 400 and 1600. The total score is the sum of the two section scores: Evidence-Based Reading and Writing, and Math. Each of these two section scores has a possible range of 200–800 ([*source*](https://satsuite.collegeboard.org/sat/scores/understanding-scores/how-scores-are-calculated)).

---

### Data Dictionary


* [`sat_2019_by_intended_college_major.csv`](./data/sat_2019_by_intended_college_major.csv): abbreviated as sat_major
* [`sat_act_by_college.csv`](./data/sat_act_by_college.csv): abbreviated as sat_college

|Feature|Type|Dataset|Description|
|---|---|---|---|
intended_college_major|string|sat_major|Majors that students intend to take
test_takers|float|sat_major|Number of test takers for each major
percent|float|sat_major|Percentage of test takers for each major
total|integer|sat_major|Total SAT scores
reading_writing|integer|sat_major|SAT reading and writing section scores
math|integer|sat_major|SAT math section scores
score_disparity|integer|sat_major|Difference between math scores and reading and writing scores
school|string|sat_college|Name of schools
number_of_applicants|integer|sat_college|Number of applicants applying for the school
accept_rate|float|sat_college|Percentage of applicants accpeted out of all applicants
sat_25th_percentile|float|sat_college|25th percentile of SAT scores
accepted_applicants|integer|sat_college|Number of accepted applicants

---

### Summary of Analysis
**Identify Patterns in Preferred Majors**
1. Compare test performance of students with or without a preferred major
1. Most popular majors
2. Most competitive majors
3. Analyze relationship between performance on different sections of SAT (math vs reading and writing) and majors

**Identify Patterns in Collge Intake**
1. Most popular colleges
2. Colleges with the greatest intake

---

### Conclusion and Recommendations

**Recommendations on Majors**
- 7% of students do not have a preferred major. Average test performance of student without preferred major is the same as the rest.
- For students who want to go for popular majors, the top 5 most popular majors are Health Professions, Business, Engineering, Biological and Biomedical Sciences, and Visual and Performing Arts. The 5 majors are pursued after by 56% of test takers.
- The most competitive majors have an average SAT scores between 1150 and 1250 (such as Mathematics and Statistics). Students may be able to consider these majors only if they manage to score within this range, minimally.
- For students who have shown strength in either math or reading and writing, they can consider majors that suit their strength. Generally, applicants strong in math tend to apply for Science majors, and applicants strong in reading and writing tend to apply for Arts majors.

**Recommendations on Colleges**
- The median of entry requirement, as estimated from the 25th percentile, is 1150. Students with a score of 1150 or above can rest assured that they are eligible to apply for at least half of the schools listed.
- For students who want to go for popular colleges, University of California is a popular choice. The 5 different University of California campuses topped in number of applicants across all colleges.
- The largest schools take in more than 30000 applicants per year, which is more than 4 times the average intake. These may be suited for students who look out for larger schools.
- Generally, schools with higher entry requirement also have greater number of applicants and lower accpetance rate. Hence, students can gauge the competitiveness of their applications based on their score range.
