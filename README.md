## TZP3 | Increased Performance Hybrid Movie Recommender System ![Awesome](https://awesome.re/badge.svg)


<p align="center"> 
<img src="img/tzp3_img.gif">
</p>

### Overview 
The main objective of this project is to contruct a system to increase performance capability in speed and accuracy updating our [first model](https://columbia.bootcampcontent.com/Zee/movies_rec_project_3) as a starting point. Please note that we are only showing the codes from the improved performances in this repository. For the first part please click on the first model link. 

---
### Project Content
1. Load Data
   1. The Datasets
      1. MovieLens
      2. OMDb
2. Data Preparation - Analysis 
   1. [Movies](https://github.com/zeexav/TZP3/blob/master/testenv/Movies.ipynb)
   2. [Ratings](https://github.com/zeexav/TZP3/blob/master/testenv/Ratings.ipynb)
3. Final Dataset 
4. Build Recommender Systems
   1. Content and Collaborative Filtering `recoSys` 
   2. SVD - Singular Value Decomposition `recoSys`
5. Hybrid RecoSys Engine 
---
### 1. Load Data
##### i. The Dataset 
##### a. [MovieLens](https://grouplens.org/datasets/movielens/) 
From MovieLens we decided to utilize the [20M dataset](http://files.grouplens.org/datasets/movielens/ml-20m-READFME.html) wich provided us 20 million ratings and 465,000 tag applications applied to 27,000 movies by 138,000 users.
##### b. [OMDb](http://www.omdbapi.com/)
We decided to utilize two datasets from OMDb, the first contains 17K  movies made from 1990, the second set contains 19K movies made from 2009 to 2018.

### 2. Data Preparation - Analysis
##### i. Movies
In summary OMDd data was gathered by using the movie titles from the MovieLens data set by calling the API. Only movie titles that matched returned information and since API matching isn't higly effective we needed to start a cleaning process to be able to join all the tables in one single data frame. For the whole cleaning process on the movie datasets please click on the link 'movies' under project content.
##### ii. Ratings 
At this stage of the project we utilized the ratings dataset from Movielens which contains approximately 27,000,000 ratings. We first explored the data doing a data analysis in order to decide the best route to take to come up with a final data set to utilize in our models. We tested different sizes on our ML models as we needed to ultimetly decide if we should slipt it based on metric or just randomly select a percentage of the data. 

### 3. Final Dataset 
After few processes of data cleaning and analysis we were able to build our final dataset. in order to build our final dataset we took into consideration our main goal, which is speed and accuracy but we also needed to be mindfull of our computational limitations as we only had our personla computers to work on. 
At first, we explored a hybrid of movie popularity with only users that have rated in between 50 and 150 movies. This process only generated 910 movies. As we were trying to undertand the lower return from our first process, we explored our avalible data further realizing that most of the users rated less than 200 movies. With that in mind we used a variety of ranges in order to come up with a perfect datase for our use. We were able to come up with an ok dataset consideration our limitations and the final dataset has 111102 movies rated by 27585 users. The optimal range ustilized was inbetween 75 and 150. 

### 4. Build Recommender Systems 
##### i. Content and Collaborative Systems 
<p align="center"> 
<img src="img/rec-systems.png">
</p>











