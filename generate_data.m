load('matlab-data-all.mat');
addpath(genpath('.'))
 
id = [64,40,30,31,32,33,43,46,55,56,68,69,70,73,75,78,81,90,93,94];
% id1 = [34,35,36,37,38,39,40,41,42,44,45,47,48,49,50,51,52,53,54,57,59,60,61,62,63,64,65,66,67,71,72,...
%     ,74,76,77,79,80,82,83,84,85,86,87,88,89,91,92,93,95,96,97];
index = 1;
index0 = 1;
sign = 0;
for i=1:length(drug_p)
    
    sign = find(id==drug_name(i));
    if sign>0
    drug_name(i) = [(id(sign))];
    X_drug_p{index} = drug_p{i}; 
    drug_id(index)=id(sign);
    index = index +1;
        
    else
    X_drug_p1{index0} = drug_p{i};
    drug_id1(index0) = drug_name(i);
    index0=index0+1;
    end
    sign = 0;
  end
index = 1;sign =0;index0=1;
for i=1:length(drug_p2)
    sign = find(id==drug_name2(i));
    if sign>0
        X_drug_p2{index} = drug_p2{i};
        drug_id2(index)=id(sign);
        index = index +1;
    else
        X_drug_p22{index0} = drug_p{i};
        drug_id22(index0)=drug_name2(i);
        index0=index0+1;
    end
    sign=0;
end

sign = 0;index=1;index0=1;
for i=1:length(placebo)
    sign = find(id==pl_name(i));
    if sign>0
    
    X_pl_p{index} = placebo{i}; 
    pl_id(index)=id(sign);
    index = index +1;
    else
        
        X_pl_p1{index0} = placebo{i};
        pl_id1(index0)=pl_name(i);
        index0=index0+1;
    end
    sign=0;
   
end
    
    
sign = 1;index = 1; index0 = 1;
for i=1:length(placebo2)
    sign = find(id==pl_name(i));
    if sign>0
        X_pl_p2{index} = placebo2{i}; 
    pl_id2(index)=id(sign);
    index = index +1;
    else   
         X_pl_p22{index0} =placebo2{i};
        pl_id22(index0)=pl_name2(i);
        index0=index0+1;
end
       sign=0;
end
   
win_size = 400 % the sliding window size you can change this sliding window size
% X_drug_p is the data for the subjects receiving THC X_pl_p is the data for the subject receiving placebo

[F1_1] = compute_corr5(X_drug_p,win_size);
[F2_1] = compute_corr5(X_pl_p,win_size);

save('data.mat')
