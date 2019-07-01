load('data.mat');
addpath(genpath('.'))

% input the ID of impaired data labelled by 1
id1 = [30,32,39,42,43,46,49,51,52,53,56,57,58,60,61,66,68,69,70,73,75,78,81,84,90,92,93,94,97];
% input the ID of placebo data labelled by 1
id2 = [30,31,32,33,34,35,36,37,40,41,42,43,45,46,48,52,56,57,58,59,60,61,...
    62,64,65,67,68,69,70,71,72,73,74,75,77,78,79,81,82,83,86,88,89,90,91,93,94,95,96];


index = 1;
index0 = 1;
sign = 0;
drug_id=[];
drug_id1 = [];
drug_id2 =[];
drug_id22 = [];

for i=1:54
    str = ( SUBJ(i).name);
    str = str(4:6);
    drug_name(i) = str2num(str);
end

for i=1:length(drug_name)
    
    sign = find(id1==drug_name(i));
    
    if length(sign)>0&&sign>0 && (length(SUBJ(i).drug_rest_post)>0)
    
    drug_name(i) = [(id1(sign))];
    X_drug_p{index} = SUBJ(i).drug_rest_post; 
    drug_id(index)=id1(sign);
    index = index +1;
        
    elseif (length(SUBJ(i).drug_rest_post)>0)
    X_drug_p1{index0} = SUBJ(i).drug_rest_post;
    drug_id1(index0) = drug_name(i);
    index0=index0+1;
    end
    sign = 0;
  end

pl_id1=[];
pl_id =[];
pl_id2 = [];
pl_id22=[];
sign = 0;index=1;index0=1;

for i=1:length(drug_name)
    sign = find(id2==drug_name(i));
    if length(sign)>0&&sign>0 && (length(SUBJ(i).placebo_rest_post)>0)
    
    X_pl_p{index} = SUBJ(i).placebo_rest_post; 
    pl_id(index)=id2(sign);
    index = index +1;
    elseif (length(SUBJ(i).placebo_rest_post)>0)
        
        X_pl_p1{index0} = SUBJ(i).placebo_rest_post; 
        pl_id1(index0)=drug_name(i);
        index0=index0+1;
    end
    sign=0;
   
end
  
% the sliding window size you can change this sliding window size
% X_drug_p is the data for the subjects receiving THC X_pl_p is the data for the subject receiving placebo
win_size = 400;
[Ft_1] = compute_corr5(X_drug_p,win_size);
[Ft_2] = compute_corr5(X_pl_p,win_size);

save('data-processed.mat')
