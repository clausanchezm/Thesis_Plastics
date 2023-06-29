function mape = calculateMAPE(actual, predicted)
%% calculates the Mean Absolute Per Error 
%TODO add ref
% from internet, divide by the actual value
     n = size(actual, 1);
     ape = abs(actual-predicted) ./actual *100;
     mape = 1/ n * sum( ape);
end