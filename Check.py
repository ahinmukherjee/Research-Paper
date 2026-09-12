import java.util.Scanner;

public class TicTacToe {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        char[][] board = new char[3][3];

        // Fill board with '-'
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '-';
            }
        }

        char player = 'X';

        for (int turn = 1; turn <= 9; turn++) {

            // Print board
            System.out.println("\nCurrent Board:");

            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    System.out.print(board[i][j] + " ");
                }
                System.out.println();
            }

            System.out.println("\nPlayer " + player + "'s turn");

            System.out.print("Enter row (1-3): ");
            int row = sc.nextInt();

            System.out.print("Enter column (1-3): ");
            int column = sc.nextInt();

            // Convert user input to array index
            row--;
            column--;

            // Check empty position
            if (board[row][column] != '-') {
                System.out.println("Position already occupied!");
                turn--;
                continue;
            }

            // Put X or O
            board[row][column] = player;

            // Check winner
            boolean win = false;

            // Check rows
            for (int i = 0; i < 3; i++) {
                if (board[i][0] == player &&
                    board[i][1] == player &&
                    board[i][2] == player) {

                    win = true;
                }
            }

            // Check columns
            for (int j = 0; j < 3; j++) {
                if (board[0][j] == player &&
                    board[1][j] == player &&
                    board[2][j] == player) {

                    win = true;
                }
            }

            // Main diagonal
            if (board[0][0] == player &&
                board[1][1] == player &&
                board[2][2] == player) {

                win = true;
            }

            // Secondary diagonal
            if (board[0][2] == player &&
                board[1][1] == player &&
                board[2][0] == player) {

                win = true;
            }

            if (win) {

                System.out.println("\nFinal Board:");

                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        System.out.print(board[i][j] + " ");
                    }
                    System.out.println();
                }

                System.out.println("\nPlayer " + player + " Wins! 🏆");

                break;
            }

            // Change player
            if (player == 'X') {
                player = 'O';
            } else {
                player = 'X';
            }
        }
    }
}






import java.awt.*;
import javax.swing.*;
import javax.swing.ImageIcon;
import java.awt.event.*;

public class Clock{
	public static void main(String args[]){
		SampleFrame sf = new SampleFrame();
		sf.setVisible(true);
		sf.setDefaultCloseOperation(3);
	}
}

class SampleFrame extends JFrame{
	public SampleFrame(){
		Toolkit kit = Toolkit.getDefaultToolkit();
		Dimension scrsize = kit.getScreenSize();
		int w= scrsize.width;
 		int h= scrsize.height;
		setSize(600, 450);
		setLocationRelativeTo(null);
		setTitle("Banking");
		setResizable(false);
		FramePanels fp=new FramePanels();
		add(fp);
	}
}

class FramePanels extends JPanel{
	Image bg;
	public void paintComponent(Graphics g){
		super.paintComponent(g);
		setBackground(new Color(255,255,255,250));
		g.drawImage(bg,0,0,getWidth(),getHeight(),this);
	}
	
	JLabel l;
	FramePanels(){
		setLayout(null);
		ImageIcon i=new ImageIcon("c:\\memory\\Ted-Gore-30-is-the-new-20.jpg");
		bg=i.getImage();

		String type[]={"Select","Admin","User"};
		JComboBox<String> comboBox=new JComboBox<>(type);
		comboBox.setBounds(30,50,150,25);
		add(comboBox);
	
		Font f= new Font("Calibri",Font.PLAIN,14);
		l=new JLabel("");
		l.setBounds(150,100,250,30);
		l.setFont(f);
		add(l);
	
		comboBox.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent ae){
				String types= (String)comboBox.getSelectedItem();
				if (types.equals("Select")) {
    					l.setText("Please select aney one.");
					}
				if(types.equals("Admin")){
					new AdminClass();
					}
				if(types.equals("User")){
					new UserClass();
					}
			}
		});
	}
}

class AdminClass extends JFrame{
	public AdminClass(){
		setSize(600, 450);
		//setLocation(w/5, h/8);
		setLocationRelativeTo(null);
		setTitle("Bankinga");
		setResizable(false);
		add(new AdminClassFramePanels());
		setVisible(true);
	}
}

class AdminClassFramePanels extends JPanel{
	public void paintComponent(Graphics g){
		super.paintComponent(g);
		setBackground(Color.blue);
	}
}

class UserClass extends JFrame{
	CardLayout cardLayout;
    	JPanel mainPanel;
	
	public UserClass(){
       		setSize(600, 450);
        		setLocationRelativeTo(null);
        		setTitle("User");
        		setResizable(false);
        		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        		// Main panel: switches between FD and RD pages
        		cardLayout = new CardLayout();
        		mainPanel = new JPanel(cardLayout);

        		mainPanel.add(new FDPanel(), "FD");
        		mainPanel.add(new RDPanel(), "RD");

        		// Menu bar 
        		JMenuBar menuBar = new JMenuBar();
		JMenu accountMenu = new JMenu("Account");

        		JRadioButtonMenuItem fdItem = new JRadioButtonMenuItem("FD");
        		JRadioButtonMenuItem rdItem = new JRadioButtonMenuItem("RD");

        		// Only one item can be selected at a time
        		ButtonGroup group = new ButtonGroup();
        		group.add(fdItem);
        		group.add(rdItem);

        		accountMenu.add(fdItem);
        		accountMenu.add(rdItem);

        		menuBar.add(accountMenu);
        		setJMenuBar(menuBar);

        		// FD selected
       	 	fdItem.addActionListener(e -> {
            			cardLayout.show(mainPanel, "FD");
            			//System.out.println("FD selected");
        		});

        		// RD selected
        		rdItem.addActionListener(e -> {
            			cardLayout.show(mainPanel, "RD");
            			//System.out.println("RD selected");
        		});

        		// Default page
        		fdItem.setSelected(true);
        		cardLayout.show(mainPanel, "FD");

        		add(mainPanel);
        		setVisible(true);
	}
}

class FDPanel extends JPanel implements ActionListener{
	JLabel amount, interest, time;
	JTextField amountField, interestField, timeField;
	JButton resultButton, resetButton;
	JLabel message;
	public FDPanel() {
        		setLayout(null);
		amount= new JLabel("Enter amount :: ");
		interest= new JLabel("Enter interest rate :: ");
		time= new JLabel("Enter time :: ");
		
		amount.setBounds(10,50,150, 25);
		interest.setBounds(10,80,150, 25);
		time.setBounds(10,110,150, 25);

		amountField= new JTextField();
		interestField= new JTextField();
		timeField= new JTextField();

		amountField.setBounds(160,50,150, 25);
		interestField.setBounds(160,80,150, 25);
		timeField.setBounds(160,110,150, 25);
	
		add(amount);
		add(interest);
		add(time);

		add(amountField);
		add(interestField);
		add(timeField);

		
		resultButton = new JButton("Click me!");
		Font f2 = new Font("serif",Font.BOLD+Font.ITALIC,18);
		resultButton.setFont(f2);
		resultButton.setBounds(85,230,150,45);
		resultButton.setBackground(Color.yellow);
		resultButton.setForeground(Color.black);
		
		resetButton = new JButton("Reset");
		resetButton.setBounds(250,230,100,45);
		resetButton.setBackground(Color.black);
		resetButton.setForeground(Color.white);
				
	
		add(resultButton);
		add(resetButton);

		message= new JLabel("");
		message.setBounds(50,290,500,25);
		message.setFont(new Font("Arial",Font.BOLD+Font.ITALIC,20));
		add(message);

		resultButton.addActionListener(this);
        		resetButton.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent ae){
				amountField.setText("");
				interestField.setText("");
				timeField.setText("");
			}
		});
   	 }
	public void actionPerformed(ActionEvent ae) {
		if(amountField.getText().isEmpty() && interestField.getText().isEmpty() && timeField.getText().isEmpty()){
			message.setText("Field cannot be empty");
		}
		else{
			try{
				double initialAmount= Double.parseDouble(amountField.getText());
				double interestRate= Double.parseDouble(interestField.getText());
				int time= Integer.parseInt(timeField.getText());

				double maturity= initialAmount* Math.pow(1+(interestRate/(4 *100.0)), 4 * time);
				message.setText("Your Maturity Amount is: Rs." +maturity);
			}
			catch(NumberFormatException nfe){
				JOptionPane.showMessageDialog(null,"Plz enter valid values");
			}
		}
		
	}
    
}

class RDPanel extends JPanel {
	public RDPanel() {
        		setBackground(new Color(255, 240, 200));
		JLabel label = new JLabel("RD Calculator Page");
        		label.setFont(new Font("Calibri", Font.BOLD, 24));
		add(label);
    	}
}
