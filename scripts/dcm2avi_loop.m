%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%CONVERT dicom data to AVI for further rtMRI analyses%
%treats each image in the current directory as a frame in one run
%Michel Belyk, February 2020
%University College London
%belykm@gmail.com
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%test for .ima and .dcm formats on only


% modified into a for loop by Ben Lang, blang@ucsd.edu

D = '/Volumes/hecate/lisaaniyat/data';
cd(D)
S = dir(fullfile(D,'*'));
N = setdiff({S([S.isdir]).name},{'.','..'}); % list of subfolders of D.

for ii = 1:numel(N)
    T = dir(fullfile(D,N{ii},'*')); % improve by specifying the file extension.
    Q = setdiff({T([T.isdir]).name},{'.','..','.DS_Store'}); % list of subfolders of D.
    % C = {T(~[T.isdir]).name}; % files in subfolder.
    for jj = 2:numel(Q)
        F = fullfile(D,N{ii},Q{1}); % do whatever with file F.
        disp(F)
        M = dir(fullfile(D,N{ii},Q{1},'*'));
        K = setdiff({M([M.isdir]).name},{'.','..','.DS_Store'});
        for kk = 1:numel(K)
            B = fullfile(D,N{ii},Q{1},K{kk});
            cd(B)

            %%%%%%%%%%%%%%%%%%%%%%%
            %%%PARAMETERS TO SET%%%
            %%%%%%%%%%%%%%%%%%%%%%%
            fps = 10;                            %frame rate frames/seconds
            output_avi = sprintf('lisaaniyat_%d.avi',kk);  %what should we call the file
            image_format = '.dcm';              %what file extension do component images have
            
            %%%%%%%%%%%%%%%
            %%%Find Data%%%
            %%%%%%%%%%%%%%%
            list_input_files = dir(strcat('*',image_format)); %list all image files
            disp(list_input_files)
            % list_input_files = B
            
            
            %%%%%%%%%%%%%%%
            %%%Loop Data%%%
            %%%%%%%%%%%%%%%
            
            %initialise video file
            writerObj = VideoWriter(output_avi);
            writerObj.FrameRate = 10;
            open(writerObj);
            
            for iFile = 1:length(list_input_files) %loop through video files
                image = list_input_files(iFile).name; %remove file enxtension and _skel tag
                disp("Processing image: " + string(iFile));
                
                frame = dicomread(image); %read image data
                frame = uint8(frame); %force class
                writeVideo(writerObj,frame);  %add to avi file
            end
            
            close(writerObj); %close video file,writing done
        end
    end
end