win_size = 400 % the sliding window size
% X_drug_p is the data for the subjects receiving THC X_pl_p is the data for the subject receiving placebo

[F1_1] = compute_corr5(X_drug_p,win_size);
[F2_1] = compute_corr5(X_pl_p,win_size);

save('data.mat')
