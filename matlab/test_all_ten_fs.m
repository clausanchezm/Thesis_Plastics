function performance = test_all_ten_fs(hyp, inff, covf, meanf, likf, fs, y, cv, gp)
       performance= zeros(size(fs,2),1);
       for i= 1: size(fs,2)
           x = fs(:,1:i);
           mape_values =  zeros(1,10);
        for k = 1 : 10 
            xtrain = x(cv.training(k),:); ytrain = y(cv.training(k),:);
            xtest = x(cv.test(k),:); ytest = y(cv.test(k),:);
            [ymu ,ys2 ,fmu, fs2, lp] = gp(hyp, @infGaussLik, meanf, covf, likf, xtrain, ytrain, xtest, ytest);
            n = size(ytest, 1);
            mape_values(k) = calculateMAPE(ytest, ymu);
        end 
            performance(i) = mean(mape_values);
       end
  
end
