function centroids = kmeans(X, k)
    %set error threshold
    min_thresh = 1e-7;
    %set maximum iterations
    max_iter = 10000000;
    %centroids
    centroids = zeros(k, 2);
    len = size(X, 2);
    nearest_c = zeros(len, 1);
    %initialise to random points
    rand_i = ceil(len * rand(k, 1));
     for i = 1:k
    centroids(i, :) = X(:, rand_i(i));
    end
 % Plot initial points (same color)
 figure;
 plot(X(1, :), X(2, :), 'kx');
 title('Puntos Iniciales');
 hold on;
 %Iteration loop
 for i = 1:max_iter
 %updated means
 new_c = zeros(size(centroids));
 %no, of points assigned to each mean
 assigned2c = zeros(k, 1);
 %Go through all data points
 for n = 1:len
 % Calculate nearest mean
 x = X(1, n);
 y = X(2, n);
 diff = ones(k, 1) * X(:, n)' - centroids;
 dist = sum(diff.^2, 2);

 [~, indx] = min(dist);
 nearest_c(n) = indx;
 new_c(indx, 1) = new_c(indx, 1) + x;
 new_c(indx, 2) = new_c(indx, 2) + y;
 assigned2c(indx) = assigned2c(indx) + 1;
 end
 %Compute new centroids
 for i = 1:k
 %Only if a centroid has data assigned
 if (assigned2c(i) > 0)
 new_c(i, :) = new_c(i, :) ./ assigned2c(i);
 end
 end
 %Early exit if error is small
 d = sum(sqrt(sum((new_c - centroids).^2, 2)));
 if d < min_thresh
 break;
 end
 centroids = new_c;
 end
 % Plot final results
 colors = 'rgb';
 figure;
 hold on;
 for i = 1:k
 cluster_points = X(:, nearest_c == i);
 plot(cluster_points(1, :), cluster_points(2, :), [colors(i), 'x']);
 end
 plot(centroids(:, 1), centroids(:, 2), 'ko', 'MarkerSize', 10, 'LineWidth',
3);
 title('Centroides con Regiones');
 hold off;
end
% Create some 2D data in 3 classes
M = 40;
c1 = ([1.9 * ones(M, 1) 0.9 * ones(M, 1)]) + randn(M, 2);
c2 = ([0.9 * ones(M, 1) 0.1 * ones(M, 1)]) + randn(M, 2);
c3 = ([0.1 * ones(M, 1) 1.9 * ones(M, 1)]) + randn(M, 2);
% Combine the data into one matrix
X = [c1; c2; c3]';
% Run the K-Means algorithm