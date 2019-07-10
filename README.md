## TZP3 | Increased Performance Hybrid Movie Recommender System ![Awesome](https://awesome.re/badge.svg)


<p align="center"> 
<img src="img/tzp3_img.gif">
</p>

### Overview 
The main objective of this project is to contruct a system to increase performance capability in speed and accuracy updating our [first model](https://columbia.bootcampcontent.com/Zee/movies_rec_project_3) as a starting point.

---
### Project Content
1. Load Data
   1. The Datasets
      1. MovieLens
      2. OMDb
2. Data Preparation
   1. [Movies](https://github.com/zeexav/TZP3/blob/master/testenv/Movies.ipynb)
   2. [Ratings](https://github.com/zeexav/TZP3/blob/master/testenv/Ratings.ipynb)
3. Build Recommender Systems
   1. Content Based `recosys` 
   2. Collaborative Filtering `recoSys`
   3. SVD - Singular Value Decomposition `recoSys`
4. Hybrid RecoSys Engine 
---
### 1. Load Data
##### 1.1 The Dataset 
##### 1.1.2 [MovieLens](https://grouplens.org/datasets/movielens/) 
From MovieLens we decided to utilize the [20M dataset](http://files.grouplens.org/datasets/movielens/ml-20m-READFME.html) wich provided us 20 million ratings and 465,000 tag applications applied to 27,000 movies by 138,000 users.
##### 1.1.3. [OMDb](http://www.omdbapi.com/)
We decided to utilize two datasets from OMDb, the first contains 17K  movies made from 1990, the second set contains 19K movies made from 2009 to 2018.

### 2. Data Preparation 
##### 2.1 Movies
In summary OMDd data was gathered by using the movie titles from the MovieLens data set by calling the API. Only movie titles that matched returned information. Since API matching isn't higly effective we started the process cleaning the data to start our joining tables procedure. For the whole cleaning process on the movie datasets please click on the link 'movies' under project content.
##### 2.1.1 OMDb





