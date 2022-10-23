model = torchvision.models.vgg19(pretrained = True)
input_lastLayer = model.classifier[6].in_features # last layer input num
model.classifier[6] = nn.Linear(input_lastLayer,10) # change last layer output
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), 
                        lr = learning_rate, 
                        momentum=0.9,
                        weight_decay=5e-4)
H = {
	"train_loss": [],
	"train_acc": [],
	"test_loss": [],
	"test_acc": []
}

progress = tqdm(len(train_loader))

for epoch in range(num_epochs):
    # set the model in training mode
    model.train()
    total_train_loss = 0
    total_test_loss = 0
    train_correct = 0
    test_correct = 0
    # loop over the training set
    for (x, y) in train_loader:
        progress.update(1)
		# send the input to the device
        (x, y) = (x.to(device), y.to(device))
		# perform a forward pass and calculate the training loss
        pred = model(x)
        loss = criterion(pred, y)
		# zero out the gradients, perform the backpropagation step,
		# and update the weights
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # add the loss to the total training loss so far and
        # calculate the number of correct predictions
        total_train_loss += loss
        train_correct += (pred.argmax(1) == y).type(torch.float).sum().item()
  
  # switch off autograd for evaluation
    with torch.no_grad():
        # set the model in evaluation mode
        model.eval()
        # loop over the validation set
        for (x, y) in test_loader:
            # send the input to the device
            (x, y) = (x.to(device), y.to(device))
            # make the predictions and calculate the validation loss
            pred = model(x)
            total_test_loss += criterion(pred, y)
            # calculate the number of correct predictions
            test_correct += (pred.argmax(1) == y).type(torch.float).sum().item()

# calculate the average training and validation loss
avg_train_loss = total_train_loss / train_total_step
avg_test_loss = total_test_loss / test_total_step

# calculate the training and validation accuracy
train_correct = train_correct / len(train_loader.dataset)
test_correct = test_correct / len(test_loader.dataset)

# update our training history
H["train_loss"].append(avg_train_loss.cpu().detach().numpy())
H["train_acc"].append(train_correct)
H["test_loss"].append(avg_test_loss.cpu().detach().numpy())
H["test_acc"].append(test_correct)

# print the model training and validation information
print("[INFO] EPOCH: {}/{}".format(epoch + 1, num_epochs))
print("Train loss: {:.6f}, Train accuracy: {:.4f}".format(avg_train_loss, train_correct))
print("Val loss: {:.6f}, Val accuracy: {:.4f}\n".format(avg_test_loss, test_correct))