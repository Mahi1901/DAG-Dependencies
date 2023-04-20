# DAG-Dependencies
An algorithm that uses the job execution logs to dynamically generate the DAG views visually using statistical techniques to achieve this goal and computing a confidence level for each line shown in the DAG view. 
To predict and optimize job execution so that they can complete before a predetermined time, it is important to know these dependencies. However, these dependencies is not always visible or obvious to the administrators. ​
 
 The CSV contains 8 unique jobs with multiple instances of every job Id. This is because a job is triggered multiple times in one day or in the coming consecutive days.
 
 Amongst the 36 attributes, we found the ‘job_name’ , ‘job_id’, ‘start_datetime’ , ‘end_datetime’ and ‘order date’ to be the ones contributing in computing the dependencies amongst the job.​
 
 
 Finding dependencies between jobs:​
         The dependencies were established using the following rules:​

        Job B is most likely to be dependent on job A if:​

        Start time of B>End time of A​

        ​

        Order date indicates if the order was placed for a job ​

        The order date of the job A should be same as the order date of job B ​

        ​

         Instances of the Job indicates the number of times the job is triggered.​

        The number of instances of job A must match with the number of instances of  job B    
        
  In the dataset, all subsets of a frequent itemset are frequent, i.e., anti-monotonicity of support measure is observed. This is the basic property of Apriori Algorithm of Machine Learning.​
  
  
  
  
  
DAG plotting of dependent jobs:​

  Parse the CSV file​

  Calculate the duration of the job​

  Create a list of edges​

  Created a Directed Acyclic Graph (DAG)​

  Used a graph layout algorithm to arrange the nodes in the DAG view​

  Compute a confidence level for each line shown in the DAG view​

  Assuming normal distribution, using z score to calculate confidence levels​

  Draw the DAG with labels and confidence​
