# Метрики в машинном обучении

Здесь я попытался представить почти полный перечень метрик используемый в машинном обучении.<br>
Метрики я описывал так, что бы было понятно как их применять, когда их применять, как их <br>
знаения интерпретировать.
## Метрики которые можно рассчитать с помощью библиотеки scikit-learn<br>
https://scikit-learn.ru/3-3-metrics-and-scoring-quantifying-the-quality-of-predictions/

## Метрики для задач классификации
### accuracy	metrics.accuracy_score	
### balanced_accuracy	metrics.balanced_accuracy_score	
### top_k_accuracy	metrics.top_k_accuracy_score	
### average_precision	metrics.average_precision_score	
### neg_brier_score	metrics.brier_score_loss	
### f1	metrics.f1_score	для двоичных целей
### f1_micro	metrics.f1_score	микро-усредненный
### f1_macro	metrics.f1_score	микро-усредненный
### f1_weighted	metrics.f1_score	средневзвешенное
### f1_samples	metrics.f1_score	по многопозиционному образцу
### neg_log_loss	metrics.log_loss требуется predict_proba поддержка
### precision etc.	metrics.precision_score	суффиксы применяются как с ‘f1’
### recall etc.	metrics.recall_score	суффиксы применяются как с ‘f1’
### jaccard etc.	metrics.jaccard_score	суффиксы применяются как с ‘f1’
### roc_auc	metrics.roc_auc_score	
### roc_auc_ovr	metrics.roc_auc_score	
### roc_auc_ovo	metrics.roc_auc_score	
### roc_auc_ovr_weighted	metrics.roc_auc_score	
### roc_auc_ovo_weighted	metrics.roc_auc_score

## Метрики для задач кластеризации
### adjusted_mutual_info_score	metrics.adjusted_mutual_info_score	
### adjusted_rand_score	metrics.adjusted_rand_score	
### completeness_score	metrics.completeness_score	
### fowlkes_mallows_score	metrics.fowlkes_mallows_score	
### homogeneity_score	metrics.homogeneity_score	
### mutual_info_score	metrics.mutual_info_score	
### normalized_mutual_info_score	metrics.normalized_mutual_info_score	
### rand_score’	metrics.rand_score	
### v_measure_score

## Метрики для задач регрессию
###explained_variance	metrics.explained_variance_score	
### max_error	metrics.max_error	
### neg_mean_absolute_error	metrics.mean_absolute_error	
### neg_mean_squared_error	metrics.mean_squared_error	
### neg_root_mean_squared_error	metrics.mean_squared_error
### neg_mean_squared_log_error metrics.mean_squared_log_error 

* RMSLE - Root Mean Squared Logarithmic Error<br>
Среднеквадратичная логарифмическая ошибка

![img.png](img.png)<br>
x - фактическое значение, y - предсказанное значение
Результат - неотрицательное значение с плавающей запятой (лучшее значение - 0.0)
Лучшей считается модель у которой RMSLE меньше. Эта метрика чаще применяется при оценке<br>
моделей интерполяции, экстраполяции.


### neg_median_absolute_error	metrics.median_absolute_error	
### r2	metrics.r2_score	
### neg_mean_poisson_deviance	metrics.mean_poisson_deviance	
### neg_mean_gamma_deviance	metrics.mean_gamma_deviance	 
### neg_mean_absolute_percentage_error

